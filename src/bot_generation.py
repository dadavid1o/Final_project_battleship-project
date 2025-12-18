import random
import pandas as pd
from src.ship_input import validate_ships

BOARD_SIZE = 10
SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def random_ship(size):
    horizontal = random.choice([True, False])
    if horizontal:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - size)
        return [(x, y + i) for i in range(size)]
    else:
        x = random.randint(0, BOARD_SIZE - size)
        y = random.randint(0, BOARD_SIZE - 1)
        return [(x + i, y) for i in range(size)]

def generate_bot_ships():
   
    while True:
        ships = []
        for size in SHIP_SIZES:
            ships.append(random_ship(size))
        if validate_ships(ships):
            return ships

def save_bot_ships_csv(ships, path="data/bot_ships.csv"):

    rows = []
    for ship_id, ship in enumerate(ships):
        for (x, y) in ship:
            rows.append([ship_id, int(x), int(y)])

    df = pd.DataFrame(rows, columns=["ship_id", "x", "y"])
    df.to_csv(path, index=False)
