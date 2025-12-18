import pandas as pd

BOARD_SIZE = 10

def empty_board():
    return [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board, title=None):
    if title:
        print(title)
    for row in board:
        print(" ".join(row))
    print()

def _neighbors8(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                yield (nx, ny)

def apply_move(board, move, ships, hits_set):

    x, y = move
    if board[x][y] in ("X", "O"):
        return ("repeat", None)

    for ship in ships:
        if move in ship:
            board[x][y] = "X"
            hits_set.add(move)
            if all(cell in hits_set for cell in ship):
                return ("hit", ship)
            return ("hit", None)

    board[x][y] = "O"
    return ("miss", None)

def mark_surroundings_after_destroyed(board, ship_cells):

    ship_set = set(ship_cells)
    for (x, y) in ship_cells:
        for (nx, ny) in _neighbors8(x, y):
            if (nx, ny) in ship_set:
                continue
            if board[nx][ny] == ".":
                board[nx][ny] = "O"

def init_game_state_csv(path="data/game_state.csv"):
    df = pd.DataFrame(columns=["turn", "player_move", "bot_move", "player_board", "bot_board"])
    df.to_csv(path, index=False)

def append_game_state(turn, player_move, bot_move, player_board, bot_board, path="data/game_state.csv"):
    row = pd.DataFrame({
        "turn": [turn],
        "player_move": [player_move],
        "bot_move": [bot_move],
        "player_board": [str(player_board)],
        "bot_board": [str(bot_board)],
    })
    try:
        old = pd.read_csv(path)
        out = pd.concat([old, row], ignore_index=True)
    except Exception:
        out = row
    out.to_csv(path, index=False)
