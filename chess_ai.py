
import os
import json
import random
from typing import Dict, Optional

import chess

try:
    import chess.engine  # optional: only needed if you pass an engine path
except Exception:  # pragma: no cover
    chess = chess  # keep import name available


PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0,
}


def simple_material_eval(board: chess.Board) -> int:
    """Fallback static evaluation (centipawns) if no UCI engine is provided."""
    score = 0
    for piece_type, value in PIECE_VALUES.items():
        score += len(board.pieces(piece_type, chess.WHITE)) * value
        score -= len(board.pieces(piece_type, chess.BLACK)) * value
    # positive = advantage white; negative = advantage black
    # Convert to "side to move" perspective:
    return score if board.turn == chess.WHITE else -score


class QTable:
    """Dict-of-dicts: {state_fen: {move_uci: q_value}} with save/load helpers."""

    def __init__(self):
        self.table: Dict[str, Dict[str, float]] = {}

    def get(self, state: str, move: str) -> float:
        return self.table.get(state, {}).get(move, 0.0)

    def set(self, state: str, move: str, value: float) -> None:
        self.table.setdefault(state, {})[move] = value

    def best_move(self, state: str, legal_moves) -> Optional[chess.Move]:
        if state not in self.table:
            return None
        # Return legal move with max Q; ignore moves not in table yet
        best = None
        best_q = float("-inf")
        for m in legal_moves:
            q = self.table[state].get(m.uci(), float("-inf"))
            if q > best_q:
                best_q, best = q, m
        return best

    def max_q(self, state: str) -> float:
        if state not in self.table or not self.table[state]:
            return 0.0
        return max(self.table[state].values())

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.table, f)

    def load(self, path: str) -> None:
        with open(path) as f:
            self.table = json.load(f)


class ChessAI:
    """
    Tiny, educational Q-learning chess bot (ε-greedy).
    - If ENGINE_PATH env or __init__ arg is provided, uses a UCI engine for reward shaping.
    - Otherwise falls back to a simple material evaluation.
    Note: This is intentionally simple and not strong. It's a learning scaffold.
    """

    def __init__(self, engine_path: Optional[str] = None, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q = QTable()

        self.engine = None
        engine_path = engine_path or os.getenv("PYBOT_ENGINE", "").strip()
        if engine_path:
            try:
                self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)  # type: ignore[attr-defined]
            except Exception as e:
                print(f"[PyBot] Engine failed to start: {e}. Falling back to material eval.")
                self.engine = None

    # -------- state helpers --------
    @staticmethod
    def state(board: chess.Board) -> str:
        # Use 'fen without clocks' for a more compact (but still unique-ish) state id
        return board.board_fen() + " " + ("w" if board.turn else "b") + " " + board.castling_xfen() + " " + (board.ep_square.__str__() if board.ep_square is not None else "-")

    def evaluate(self, board: chess.Board) -> float:
        if self.engine is not None:
            try:
                info = self.engine.analyse(board, chess.engine.Limit(time=0.1))  # type: ignore[attr-defined]
                cp = info["score"].relative.score(mate_score=10000)
                if cp is None:
                    return 0.0
                return float(cp)
            except Exception:
                pass
        return float(simple_material_eval(board))

    # -------- policy --------
    def choose_move(self, board: chess.Board) -> chess.Move:
        s = self.state(board)
        legal = list(board.legal_moves)

        # Explore
        if random.random() < self.epsilon:
            return random.choice(legal)

        # Exploit
        best = self.q.best_move(s, legal)
        if best is None:
            return random.choice(legal)
        return best

    # -------- learning --------
    def update(self, s: str, a: chess.Move, reward: float, s_next: str):
        old_q = self.q.get(s, a.uci())
        target = reward + self.gamma * self.q.max_q(s_next)
        new_q = old_q + self.alpha * (target - old_q)
        self.q.set(s, a.uci(), new_q)

    def close(self):
        try:
            if self.engine is not None:
                self.engine.quit()  # type: ignore[attr-defined]
        except Exception:
            pass
