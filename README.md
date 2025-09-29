<p align="center">
  <img src="https://github.com/user-attachments/assets/905ead19-3392-4fe8-bbb6-8904cef3ae3b" alt="CheckMate animation" width="560" style="border-radius:14px;"/>
</p>

<h1 align="center">CheckMate — PyBot Chess AI Coach</h1>

<p align="center">
  <em>Play. Watch. Learn. An interactive chess coach built with Python + Pygame, powered by Stockfish.</em>
</p>

---

## What it is
CheckMate is a teaching-first chess app: you can play the bot, watch self-play, or train with beginner-friendly overlays. It explains blunders plainly, shows best-move arrows, highlights center control & development, and warns when you’ve left pieces hanging.

### Highlights
- Stockfish-backed evaluations + principal variation (multi-move plan)
- Toggleable coaching overlays:
  - **Hints (H):** Best-move arrows, blunder vs. better alternative
  - **Openings (O):** Center control & early development tips
  - **Tactics (T):** Undefended (“hanging”) piece warnings
- Human vs Bot, **Self-play**, or **Bot vs Bot Duel**
- Click-to-move with reselect support
- Sidebar with eval bar, commentary, scoreboard

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c8ef489-b939-445f-ada1-c6d9079e2a15" alt="Banner" height="500" width="500" style="border-radius:12px;"/>
</p>

---

# Features
- Full chessboard with PNG sprites (pieces-png/ folder included)
- Stockfish-backed evaluations + principal variation (next-move plan)
- Beginner overlays (Hints, Openings, Tactics) toggleable in-game
- Click-to-move with reselect support (change piece before committing)
- Scoreboard for wins, draws, losses
- Human vs Bot, Self-play, or Bot vs Bot Duel
- Sidebar shows evaluation, plan, and teaching commentary


<p align="center">
  <img src="https://github.com/user-attachments/assets/52d17797-c503-499c-b7a7-42f1c98ad0ec" alt="Banner" height="500" width="500" style="border-radius:12px;"/>
</p>

### Installation

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



## Usage

Run with defaults (human as White):

python3 play_pygame_pro.py --mode human --side white

# Human as White
python3 src/play_pygame_pro.py --mode human --side white

# Watch AI self-play
python3 src/play_pygame_pro.py --mode self

# Bot vs Bot duel
python3 src/play_pygame_pro.py --mode duel


## Options
	•	--side white|black — color (human mode)
	•	--ms N — delay per bot move in ms (default 300)
	•	--engine PATH — Stockfish path (overrides auto-detect)
	•	--w N / --h N — optional window clamp if your monitor is small


### Modes
	•	--mode human → Play against the bot
	•	--mode self → Watch AI self-play
	•	--mode duel → Bot vs Bot duel (slightly different styles)

### Options
	•	--side white|black → Choose your color (if human mode)
	•	--ms N → Milliseconds delay per bot move (default 300)
	•	--engine PATH → Explicit path to Stockfish (auto-detected if omitted)


## Assets

All chess piece sprites are loaded from /pieces-png/.
The loader automatically handles aliases like rook.png, rook4.png, bpawn.png, etc.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2ecf05c6-d4bf-4071-b10b-7013a9d79e3b" alt="Banner" height="500" width="500" style="border-radius:12px;"/>
</p>

## How It Teaches
- Explains your moves vs. engine best: “That was a blunder. Knight f3 was stronger because it develops a piece and controls the center.”
- Highlights tactical oversights: undefended pieces flash red.
- Suggests opening principles: “Try playing e4/d4 to control the center. Develop knights and bishops first.”
- Shows a multi-move “Plan” (principal variation) for strategy context.


<p align="center">
  <img src="https://github.com/user-attachments/assets/fe20bd7a-0be7-4c57-9ed5-49d5b2e6ac8e" alt="Banner" height="500" width="500" style="border-radius:12px;"/>
</p>





### MIT License.
Stockfish engine is GPL and installed separately; this project does not redistribute it.




<p align="center">
  <img src="https://github.com/user-attachments/assets/8f9893cb-67cb-4d58-8bee-5701a3e82038" alt="Banner" height="400" width="400" style="border-radius:12px;"/>
</p>






