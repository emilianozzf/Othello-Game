from tile import Tile


class Tiles:
    """A collection of tiles"""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = 100
        self.ROWS = self.HEIGHT // self.SPACING
        self.COLS = self.WIDTH // self.SPACING

        # Create an empty collection of tiles
        self.tiles = [[None for j in range(self.COLS)]
                      for i in range(self.ROWS)]

        # Put 4 tiles at the beginning of the game
        self.tiles[self.ROWS//2-1][self.COLS//2-1] = Tile(
            self.COLS//2-1, self.ROWS//2-1, 1
        )
        self.tiles[self.ROWS//2][self.COLS//2] = Tile(
            self.COLS//2, self.ROWS//2, 1
        )
        self.tiles[self.ROWS//2-1][self.COLS//2] = Tile(
            self.COLS//2, self.ROWS//2-1, 0
        )
        self.tiles[self.ROWS//2][self.COLS//2-1] = Tile(
            self.COLS//2-1, self.ROWS//2, 0
        )

        self.tile_counts = {"black": 2, "white": 2}

    def display(self):
        """Draw a collection of tiles"""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j]:
                    self.tiles[i][j].display()

    def put_tile(self, x, y, color):
        """Put a new tile in the collection"""
        row = y // self.SPACING
        col = x // self.SPACING
        self.tiles[row][col] = Tile(
            col, row, color
        )
        if color == 0:
            self.tile_counts["black"] += 1
        else:
            self.tile_counts["white"] += 1
