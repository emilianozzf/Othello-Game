class Player1:
    """Player1 class"""
    def __init__(self, board, game_controller):
        self.board = board
        self.gc = game_controller

    def move(self, x, y):
        """Handle keyboard input for Player1"""
        self.board.put_tile(x, y, 0)
