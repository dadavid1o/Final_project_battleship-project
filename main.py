from src.ship_input import read_player_ships, validate_ships, save_ships_csv
from src.bot_generation import generate_bot_ships, save_bot_ships_csv
from src.gameplay import empty_board, print_board, init_game_state_csv

def main():
    # 1
    player_ships = read_player_ships()
    if not validate_ships(player_ships):
        print("Invalid ship placement. Please try again.")
        return
    save_ships_csv(player_ships, "data/player_ships.csv")
    print("Saved: data/player_ships.csv")

    # 2
    bot_ships = generate_bot_ships()
    save_bot_ships_csv(bot_ships, "data/bot_ships.csv")
    print("Saved: data/bot_ships.csv")

    # 3
    init_game_state_csv("data/game_state.csv")
    print("Initialized: data/game_state.csv")

    player_board = empty_board()
    bot_board = empty_board()
    print_board(player_board, title="Player view board (starter):")
    print_board(bot_board, title="Bot view board (starter):")

    print("Parts 1–3 are ready. Part 4 (loop) and Part 5 (smart bot) are not implemented.")

if __name__ == "__main__":
    main()
