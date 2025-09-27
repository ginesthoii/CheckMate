#!/bin/bash
# Simple launcher for PyBot Chess

MODE="human"
SIDE="white"
ENGINE=""
MS=300

# Usage help
usage() {
  echo "Usage: $0 [mode] [side] [--engine /path/to/stockfish] [--ms delay]"
  echo "  mode: human | self | duel      (default: human)"
  echo "  side: white | black            (default: white, only used in human mode)"
  echo "Examples:"
  echo "  $0 human white"
  echo "  $0 human black"
  echo "  $0 self"
  echo "  $0 duel"
  echo "  $0 duel --engine /usr/local/bin/stockfish"
}

# Parse args
if [[ $# -ge 1 ]]; then
  case "$1" in
    human|self|duel) MODE=$1 ;;
    -h|--help) usage; exit 0 ;;
  esac
  shift
fi

if [[ "$MODE" == "human" && $# -ge 1 ]]; then
  case "$1" in
    white|black) SIDE=$1 ;;
  esac
  shift
fi

# Pass through extra options like --engine or --ms
EXTRA="$@"

# Run
echo "Launching PyBot Chess: mode=$MODE side=$SIDE ms=$MS $EXTRA"
python3 play_pygame_pro.py --mode "$MODE" --side "$SIDE" $EXTRA