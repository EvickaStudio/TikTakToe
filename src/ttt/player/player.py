class Player:
    """
    A class to represent a player in a Tic-Tac-Toe game.

    Attributes
    ----------
    name : str
        The name of the player.
    symbol : str
        The symbol (either 'X' or 'O') representing the player.

    Methods
    -------
    __init__(name: str, symbol: str) -> None
        Initializes the player with a name and a symbol.
    """
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol