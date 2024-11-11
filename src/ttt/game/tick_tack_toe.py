"""
A class to represent a Tic-Tac-Toe game.

Attributes
----------
board : list
    The game board.
current_player : Player
    The current player.
player_1 : Player
    The first player.
player_2 : Player
    The second player.
winner : Player or None
    The winner of the game.

Methods
-------
__init__(player_1: Player, player_2: Player) -> None
    Initializes the game with two players.
add_move(player: Player, position: int) -> None
    Adds a move to the board.
check_winner() -> None
    Checks if there is a winner.
switch_player() -> None
    Switches the current player.
check_draw() -> bool
    Checks if the game is a draw.
__str__() -> str
    Returns the board as a formatted string.
"""

from src.ttt.player import Player


class TickTackToe:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        """
        Initializes the game with two players.

        Parameters
        ----------
        player_1 : Player
            The first player.
        player_2 : Player
            The second player.

        Returns
        -------
        None
        """
        # Initialize the board
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        # Set the current player
        self.current_player = player_1
        self.player_1 = player_1
        self.player_2 = player_2

        # Set the winner to None
        self.winner = None

    def add_move(self, player: Player, position: int) -> None:
        """
        Adds a move to the board.

        Parameters
        ----------
        player : Player
            The player making the move.
        position : int
            The position on the board.

        Returns
        -------
        None
        """
        # Check if the given position is valid
        if self.board[position] != " ":
            print("Invalid move")
            return
        # Add the move to the board
        self.board[position] = player.symbol
        # Check if there is a winner
        self.check_winner()
        # If there is no winner, switch the player
        if not self.winner:
            self.switch_player()

    def check_winner(self) -> None:
        """
        Checks if there is a winner.

        Evaluates all possible winning combinations on the board.
        If a winning combination is found, sets the winner to the current player
        and prints the winner's name.

        Returns
        -------
        None
        """
        # All possible winning combinations
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        # Check for all winning combinations
        for _ in winning_combinations:
            # Check if the three positions are the same and not empty
            if self.board[_[0]] == self.board[_[1]] == self.board[_[2]] != " ":
                # Set the winner
                self.winner = self.current_player
                print(f"Winner: {self.winner.name}")
                return
            else:
                return

    def switch_player(self) -> None:
        """
        Switches the current player.

        Toggles the current player between player_1 and player_2.

        Returns
        -------
        None
        """
        # Switch the current player
        self.current_player = (
            self.player_1 if self.current_player == self.player_2 else self.player_2
        )

    def check_draw(self) -> bool:
        """
        Checks if the game is a draw.

        Returns
        -------
        bool
            True if there are no empty spaces on the board, indicating a draw. False otherwise.
        """
        return " " not in self.board

    # for printing the current status
    def __str__(self) -> None:
        """
        Returns the board as a formatted string.

        Returns
        -------
        str
            The current state of the board.
        """
        board_str = ""
        for i in range(9):
            board_str += f" {self.board[i]} "
            # for the edges
            if (i + 1) % 3 == 0:
                board_str += "\n"
                # for the border between the lines
                if i < 6:
                    board_str += "-----------\n"
            # else
            else:
                board_str += "|"
        return board_str
