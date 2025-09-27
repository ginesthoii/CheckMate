
import argparse
import json
import random
from pathlib import Path

import chess

from chess_ai import ChessAI

def play_training_game(bot: ChessAI, opponent="random", max_moves=200):
    board = chess.Board()
    history = []
    while not board.is_game_over() and len(history) < max_moves:
        s = bot.state(board)

        if board.turn == chess.WHITE:
            move = bot.choose_move(board)
        else:
            # Opponent policy
            if opponent == "random":
                move = random.choice(list(board.legal_moves))
            else:
                move = random.choice(list(board.legal_moves))

        board.push(move)

        # Reward after bot's own move only (skip after opponent)
        if board.turn == chess.BLACK:  # just played as WHITE
            reward = bot.evaluate(board) / 100.0  # scale
            s_next = bot.state(board)
            bot.update(s, move, reward, s_next)
            history.append((s, move.uci(), reward))

    # Final terminal reward
    if board.is_game_over():
        result = board.result()  # '1-0', '0-1', '1/2-1/2'
        terminal_reward = {"1-0": 1.0, "0-1": -1.0}.get(result, 0.0)
    else:
        terminal_reward = 0.0
    if history:
        s_last, a_last, _ = history[-1]
        bot.update(s_last, chess.Move.from_uci(a_last), terminal_reward, bot.state(board))

    return board.result() if board.is_game_over() else "unfinished"

def main():
    p = argparse.ArgumentParser(description="Train PyBot (tiny Q-learning chess)")
    p.add_argument("--engine", type=str, default="", help="Path to a UCI engine (e.g., stockfish). Optional.")
    p.add_argument("--games", type=int, default=20, help="Number of self-play (vs random) games to train.")
    p.add_argument("--save", type=str, default="pybot_qtable.json", help="Where to save learned Q-table.")
    p.add_argument("--load", type=str, default="", help="Load an existing Q-table JSON (optional).")
    p.add_argument("--epsilon", type=float, default=0.2, help="Exploration rate.")
    p.add_argument("--alpha", type=float, default=0.1, help="Learning rate.")
    p.add_argument("--gamma", type=float, default=0.9, help="Discount factor.")
    args = p.parse_args()

    bot = ChessAI(engine_path=args.engine or None, alpha=args.alpha, gamma=args.gamma, epsilon=args.epsilon)

    # Optional: load prior knowledge
    if args.load and Path(args.load).exists():
        bot.q.load(args.load)
        print(f"[PyBot] Loaded Q-table from {args.load}")

    wins = draws = losses = 0
    for g in range(1, args.games + 1):
        result = play_training_game(bot)
        if result == "1-0":
            wins += 1
        elif result == "0-1":
            losses += 1
        else:
            draws += 1

        # Light epsilon decay so it starts exploring then exploits a bit more
        bot.epsilon = max(0.01, bot.epsilon * 0.98)

        if g % 5 == 0 or g == args.games:
            Path(args.save).parent.mkdir(parents=True, exist_ok=True)
            bot.q.save(args.save)
            print(f"[PyBot] Game {g}/{args.games} → W:{wins} D:{draws} L:{losses} | ε={bot.epsilon:.3f} | saved {args.save}")

    bot.close()
    print("[PyBot] Done. Q-table saved to", args.save)

if __name__ == "__main__":
    main()
