<p align="center">
  <img src="https://github.com/user-attachments/assets/87a6ec46-ce86-461f-bcd7-f7bafb46f9f8" alt="Banner" width="300" height="300" style="border-radius:15px;"/>
</p>


<h1>CheckMate — PyBot Chess AI Coach</h1>

An interactive chess coach written in Python with Pygame and powered by Stockfish.
Play against the bot, watch self-play, or train by turning on beginner-friendly coaching overlays:
- Hints (H): Shows best-move arrows, explains blunders vs. better alternatives.
- Openings (O): Highlights center squares and recommends early development.
- Tactics (T): Warns about hanging (undefended) pieces.
- Rationale panel: Explains why moves are good/bad in natural language.



Features
- Full chessboard with PNG sprites (pieces-png/ folder included)
- Stockfish-backed evaluations + principal variation (next-move plan)
- Beginner overlays (Hints, Openings, Tactics) toggleable in-game
- Click-to-move with reselect support (change piece before committing)
- Scoreboard for wins, draws, losses
- Human vs Bot, Self-play, or Bot vs Bot Duel
- Sidebar shows evaluation, plan, and teaching commentary


 Installation

git clone <this-repo-url>
cd CheckMate

# Install dependencies
pip install pygame python-chess

Install Stockfish (recommended)

On macOS with Homebrew:

brew install stockfish

On Ubuntu/Debian:

sudo apt install stockfish

Check path:

which stockfish
# e.g. /opt/homebrew/bin/stockfish



Usage

Run with defaults (human as White):

python3 play_pygame_pro.py --mode human --side white

Modes
	•	--mode human → Play against the bot
	•	--mode self → Watch AI self-play
	•	--mode duel → Bot vs Bot duel (slightly different styles)

Options
	•	--side white|black → Choose your color (if human mode)
	•	--ms N → Milliseconds delay per bot move (default 300)
	•	--engine PATH → Explicit path to Stockfish (auto-detected if omitted)



Controls

Key	Action
H	Toggle Hints (best move arrow, blunder explanation)
O	Toggle Openings coach (center + development highlights)
T	Toggle Tactics coach (hanging pieces alerts)
[ / ]	Slow down / speed up bot moves
R	Reset board
ESC	Quit


Assets

All chess piece sprites are loaded from /pieces-png/.
The loader automatically handles aliases like rook.png, rook4.png, bpawn.png, etc.



How It Teaches
- Explains your moves vs. engine best: “That was a blunder. Knight f3 was stronger because it develops a piece and controls the center.”
- Highlights tactical oversights: undefended pieces flash red.
- Suggests opening principles: “Try playing e4/d4 to control the center. Develop knights and bishops first.”
- Shows a multi-move “Plan” (principal variation) for strategy context.



MIT License.
Stockfish engine is GPL and installed separately; this project does not redistribute it.


