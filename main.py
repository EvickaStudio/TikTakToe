from src import TickTackToe, Player
import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # get player names
    player_1_name = input("Enter name for Player 1 (X): ")
    player_2_name = input("Enter name for Player 2 (O): ")

    # Init
    player_1 = Player(player_1_name, "X")
    player_2 = Player(player_2_name, "O")
    game = TickTackToe(player_1, player_2)

    # Game loop
    # if there is no winner and no draw, keep playing
    while not game.winner and not game.check_draw():
        # print the game board
        print(game)
        try:
            # for simplicity, use 1-9 to represent the position on the board instead of 0-8 or (x, y)
            position = (
                int(input(f"{game.current_player.name}'s turn. Enter position (1-9): "))
                - 1
            )
            # Error handling
            if position < 0 or position > 8:
                print("Invalid position. Try again.")
                continue
            # add the move to the board
            game.add_move(game.current_player, position)
            
            # clear the screen
            cls()
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    print(game)
    if game.winner:
        print(f"Congratulations {game.winner.name}! You have won the game.")
    elif game.check_draw:
        print("It's a draw!")
    else:
        print("Something went wrong :c")


if __name__ == "__main__":
    main()
