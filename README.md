

<p align="center">
  <img src="https://github.com/user-attachments/assets/905ead19-3392-4fe8-bbb6-8904cef3ae3b" alt="gif" width="600" height="600" style="border-radius:15px;"/>
</p>

<h1 align="center">
CheckMate — PyBot Chess AI Coach
</h1>

<br>

### An interactive chess coach written in Python with Pygame and powered by Stockfish.
### Play against the bot, watch self-play, or train by turning on beginner-friendly coaching overlays:
- Hints (H): Shows best-move arrows, explains blunders vs. better alternatives.
- Openings (O): Highlights center squares and recommends early development.
- Tactics (T): Warns about hanging (undefended) pieces.
- Rationale panel: Explains why moves are good/bad in natural language.



# Features
- Full chessboard with PNG sprites (pieces-png/ folder included)
- Stockfish-backed evaluations + principal variation (next-move plan)
- Beginner overlays (Hints, Openings, Tactics) toggleable in-game
- Click-to-move with reselect support (change piece before committing)
- Scoreboard for wins, draws, losses
- Human vs Bot, Self-play, or Bot vs Bot Duel
- Sidebar shows evaluation, plan, and teaching commentary


<p align="center">
  <img src="https://github.com/user-attachments/assets/87a6ec46-ce86-461f-bcd7-f7bafb46f9f8" alt="Banner" width="200" height="200" style="border-radius:15px;"/>
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

### Modes
	•	--mode human → Play against the bot
	•	--mode self → Watch AI self-play
	•	--mode duel → Bot vs Bot duel (slightly different styles)

### Options
	•	--side white|black → Choose your color (if human mode)
	•	--ms N → Milliseconds delay per bot move (default 300)
	•	--engine PATH → Explicit path to Stockfish (auto-detected if omitted)



### Controls

Key	Action
H	Toggle Hints (best move arrow, blunder explanation)
O	Toggle Openings coach (center + development highlights)
T	Toggle Tactics coach (hanging pieces alerts)
[ / ]	Slow down / speed up bot moves
R	Reset board
ESC	Quit


## Assets

All chess piece sprites are loaded from /pieces-png/.
The loader automatically handles aliases like rook.png, rook4.png, bpawn.png, etc.



## How It Teaches
- Explains your moves vs. engine best: “That was a blunder. Knight f3 was stronger because it develops a piece and controls the center.”
- Highlights tactical oversights: undefended pieces flash red.
- Suggests opening principles: “Try playing e4/d4 to control the center. Develop knights and bishops first.”
- Shows a multi-move “Plan” (principal variation) for strategy context.



### MIT License.
Stockfish engine is GPL and installed separately; this project does not redistribute it.



![Image](https://github.com/user-attachments/assets/09e8e622-5bf0-4b26-a94d-ee5b6f298969)



<img width="1001" height="695" alt="Image" src="https://github.com/user-attachments/assets/8c8ef489-b939-445f-ada1-c6d9079e2a15" />
<img width="1005" height="706" alt="Image" src="https://github.com/user-attachments/assets/52d17797-c503-499c-b7a7-42f1c98ad0ec" />
<img width="992" height="662" alt="Image" src="https://github.com/user-attachments/assets/fe20bd7a-0be7-4c57-9ed5-49d5b2e6ac8e" />
<img width="732" height="647" alt="Image" src="https://github.com/user-attachments/assets/6b8cff97-d515-4015-9b77-30c5454a2f80" />
<img width="1001" height="697" alt="Image" src="https://github.com/user-attachments/assets/2ecf05c6-d4bf-4071-b10b-7013a9d79e3b" />
<img width="1000" height="703" alt="Image" src="https://github.com/user-attachments/assets/8f9893cb-67cb-4d58-8bee-5701a3e82038" />

![Image](https://github.com/user-attachments/assets/7161c6b4-fdfc-44c0-bc8b-53a5e705b42d)
