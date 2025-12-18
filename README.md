# Battleship — Parts 1–3

Implemented:
- Part 1: Player ship input + validation + save to CSV (pandas)
- Part 2: Bot ship generation + save to CSV (pandas)
- Part 3: Game state tracking helpers + initialization CSV (pandas)

## Run
```bash
python main.py
```

## Input format (Part 1)
Enter ships one per line as a list of (x,y) tuples. Empty line to finish.

Example:
```
[(0,0),(0,1),(0,2),(0,3)]
[(2,2),(2,3),(2,4)]
[(5,5)]
...
```

## CSV formats
- data/player_ships.csv and data/bot_ships.csv:
  columns: ship_id, x, y

- data/game_state.csv:
  columns: turn, player_move, bot_move, player_board, bot_board
