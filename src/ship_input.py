import pandas as pd

BOARD_SIZE = 10
SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def _neighbors8(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                yield (nx, ny)

def _is_straight_contiguous(ship):
    # ship: list of (x,y)
    if len(ship) <= 1:
        return True
    xs = [c[0] for c in ship]
    ys = [c[1] for c in ship]
    if len(set(xs)) == 1:
        y_sorted = sorted(ys)
        return y_sorted == list(range(y_sorted[0], y_sorted[0] + len(ship)))
    if len(set(ys)) == 1:
        x_sorted = sorted(xs)
        return x_sorted == list(range(x_sorted[0], x_sorted[0] + len(ship)))
    return False

def validate_ships(ships):

    if not isinstance(ships, list):
        return False

    sizes = []
    occupied = set()

    for ship in ships:
        if not isinstance(ship, list) or len(ship) == 0:
            return False

        try:
            ship_cells = [(int(x), int(y)) for (x, y) in ship]
        except Exception:
            return False

        
        if len(set(ship_cells)) != len(ship_cells):
            return False

      
        for (x, y) in ship_cells:
            if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
                return False

       
        if not _is_straight_contiguous(ship_cells):
            return False

        sizes.append(len(ship_cells))

       
        for c in ship_cells:
            if c in occupied:
                return False
        occupied.update(ship_cells)

    
    if sorted(sizes) != sorted(SHIP_SIZES):
        return False    

    all_cells_to_ship = {}
    for i, ship in enumerate(ships):
        ship_cells = [(int(x), int(y)) for (x, y) in ship]
        for c in ship_cells:
            all_cells_to_ship[c] = i

    for (x, y), sid in all_cells_to_ship.items():
        for (nx, ny) in _neighbors8(x, y):
            if (nx, ny) in all_cells_to_ship and all_cells_to_ship[(nx, ny)] != sid:
                return False

    return True

def _parse_cell(s):
    s = s.strip().upper()
    col = s[0]                      
    row = int(s[1:])                
    y = ord(col) - ord("A")       
    x = row - 1                     
    return (x, y)

def read_player_ships():
    ships = []
    print("Enter ships (one per line) like: A1 A2 A3. Empty line to finish.")
    while True:
        line = input().strip()
        if line == "":
            break
        parts = line.split()
        ship = [_parse_cell(p) for p in parts]
        ships.append(ship)
    return ships


def save_ships_csv(ships, path):
    rows = []
    for ship_id, ship in enumerate(ships):
        for (x, y) in ship:
            rows.append([ship_id, int(x), int(y)])
    df = pd.DataFrame(rows, columns=["ship_id", "x", "y"])
    df.to_csv(path, index=False)

def load_ships_csv(path):
    """Load ships from CSV (ship_id, x, y) back into list-of-ships format."""
    df = pd.read_csv(path)
    ships = []
    for ship_id in sorted(df["ship_id"].unique()):
        part = df[df["ship_id"] == ship_id][["x", "y"]].values.tolist()
        ships.append([(int(x), int(y)) for x, y in part])
    return ships
