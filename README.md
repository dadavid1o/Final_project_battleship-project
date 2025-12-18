# Battleship 

Implemented:
- Part 1: Player ship input + validation + save to CSV (pandas)
- Part 2: Bot ship generation + save to CSV (pandas)
- Part 3: Game state tracking helpers + initialization CSV (pandas)

## Run
python main.py

## Input format (Part 1)
Ships are entered one per line using battleship-style coordinates.

Each cell is written as:
- Letter A–J (column)
- Number 1–10 (row)

Cells of one ship are separated by spaces.
Empty line finishes input.

Example:
A1 B1 C1 D1
A3 B3 C3
A5 B5 C5
A7 B7
A9 B9
F1
F3
F5
F7
F9

## CSV formats
data/player_ships.csv and data/bot_ships.csv:
columns: ship_id, x, y

data/game_state.csv:
columns: turn, player_move, bot_move, player_board, bot_board
