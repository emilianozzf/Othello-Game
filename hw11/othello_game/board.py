from tiles import Tiles


class Board:
    """Draw the board and handle interaction between players and tiles"""
    def __init__(self, WIDTH, HEIGHT, game_controller):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = 100
        self.ROWS = self.HEIGHT // self.SPACING
        self.COLS = self.WIDTH // self.SPACING
        self.gc = game_controller
        self.tiles = Tiles(WIDTH, HEIGHT)

    def display(self):
        """Display the board"""
        # Make necessary per-frame updates
        self.update()

        # Display the tiles
        self.tiles.display()

        # Draw the board lines
        stroke(0)
        strokeWeight(3)
        for i in range(self.ROWS-1):
            line(0, (i + 1) * 100, self.WIDTH, (i + 1) * 100)
        for j in range(self.COLS-1):
            line((j + 1) * 100, 0, (j + 1) * 100, self.HEIGHT)

    def put_tile(self, x, y, color):
        """Put a new tile on the board"""
        row = y // self.SPACING
        col = x // self.SPACING
        if not self.tiles.tiles[row][col]:
            self.tiles.put_tile(x, y, color)
            self.gc.player1_turn = not self.gc.player1_turn

    def update(self):
        """Make necessary per-frame updates"""
        # Check whether the board are filled
        player1_score = self.tiles.tile_counts["black"]
        player2_score = self.tiles.tile_counts["white"]
        if player1_score + player2_score == self.ROWS * self.COLS:
            self.gc.players_tie = True
            self.gc.player1_score = player1_score
            self.gc.player2_score = player2_score
