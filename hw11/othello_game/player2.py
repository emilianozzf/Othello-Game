class Player2:
    """Player2 class"""
    def __init__(self, board, game_controller):
        self.board = board
        self.gc = game_controller

    def move(self, x, y):
        """Handle keyboard input for Player2"""
        self.board.put_tile(x, y, 1)
