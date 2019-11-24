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

    def update(self):
        """Make necessary per-frame updates"""
        # Check whether the board has legal moves left per-frame
        black_legal_moves_left = False
        white_legal_moves_left = False
        for i in range(len(self.tiles.tiles)):
            for j in range(len(self.tiles.tiles[i])):
                if ((not black_legal_moves_left) and
                   (self.search_legal_moves(i, j, 0))):
                    black_legal_moves_left = True
                if ((not white_legal_moves_left) and
                   (self.search_legal_moves(i, j, 1))):
                    white_legal_moves_left = True

        if not black_legal_moves_left:
            self.gc.player1_no_legal_moves_left = True
        if not white_legal_moves_left:
            self.gc.player2_no_legal_moves_left = True
        if (not black_legal_moves_left) and (not white_legal_moves_left):
            self.gc.game_over = True

        # Collect the players scores per-frame
        self.gc.player1_score = self.tiles.tile_counts["black"]
        self.gc.player2_score = self.tiles.tile_counts["white"]

    def put_tile(self, x, y, color):
        """Put a new tile on the board if the move is legal"""
        row = y // self.SPACING
        col = x // self.SPACING
        legal_moves = self.search_legal_moves(row, col, color)

        # Check if the move is legal
        if legal_moves:
            # Put a tile if the move is legal
            self.tiles.put_tile(x, y, color)
            # Flip the corresponding opposing tiles
            self.tiles.flip_tiles(color, legal_moves)
            # It's another player's turn
            self.gc.player1_turn = not self.gc.player1_turn

    def search_legal_moves(self, row, col, color):
        """Determine if the current move is legal"""
        # Keep track of the lagality of all the 8 directions
        legal_moves = {}

        # Check if the square is empty
        if not self.tiles.tiles[row][col]:
            # Check if it would end up flipping any opposing tiles
            # Check top
            potential_moves = []
            row_i = row
            while ((row_i - 1 != -1) and
                   (self.tiles.tiles[row_i-1][col]) and
                   (self.tiles.tiles[row_i-1][col].color != color)):
                potential_moves.append((row_i-1, col))
                row_i -= 1

            if ((potential_moves) and
               (row_i - 1 != -1) and
               (self.tiles.tiles[row_i-1][col]) and
               (self.tiles.tiles[row_i-1][col].color == color)):
                legal_moves["top"] = potential_moves
                row_i -= 1

            # Check left
            potential_moves = []
            col_i = col
            while ((col_i - 1 != -1) and
                   (self.tiles.tiles[row][col_i-1]) and
                   (self.tiles.tiles[row][col_i-1].color != color)):
                potential_moves.append((row, col_i-1))
                col_i -= 1

            if ((potential_moves) and
               (col_i - 1 != -1) and
               (self.tiles.tiles[row][col_i-1]) and
               (self.tiles.tiles[row][col_i-1].color == color)):
                legal_moves["left"] = potential_moves
                col_i -= 1

            # Check bottom
            potential_moves = []
            row_i = row
            while ((row_i + 1 < self.ROWS) and
                   (self.tiles.tiles[row_i+1][col]) and
                   (self.tiles.tiles[row_i+1][col].color != color)):
                potential_moves.append((row_i+1, col))
                row_i += 1

            if ((potential_moves) and
               (row_i + 1 < self.ROWS) and
               (self.tiles.tiles[row_i+1][col]) and
               (self.tiles.tiles[row_i+1][col].color == color)):
                legal_moves["bottom"] = potential_moves
                row_i += 1

            # Check right
            potential_moves = []
            col_i = col
            while ((col_i + 1 < self.COLS) and
                   (self.tiles.tiles[row][col_i+1]) and
                   (self.tiles.tiles[row][col_i+1].color != color)):
                potential_moves.append((row, col_i+1))
                col_i += 1

            if ((potential_moves) and
               (col_i + 1 < self.COLS) and
               (self.tiles.tiles[row][col_i+1]) and
               (self.tiles.tiles[row][col_i+1].color == color)):
                legal_moves["right"] = potential_moves
                col_i += 1

            # Check topleft
            potential_moves = []
            row_i = row
            col_i = col
            while ((row_i - 1 != -1) and (col_i - 1 != -1) and
                   (self.tiles.tiles[row_i-1][col_i-1]) and
                   (self.tiles.tiles[row_i-1][col_i-1].color != color)):
                potential_moves.append((row_i-1, col_i-1))
                row_i -= 1
                col_i -= 1

            if ((potential_moves) and
               (row_i - 1 != -1) and (col_i - 1 != -1) and
               (self.tiles.tiles[row_i-1][col_i-1]) and
               (self.tiles.tiles[row_i-1][col_i-1].color == color)):
                legal_moves["topleft"] = potential_moves
                row_i -= 1
                col_i -= 1

            # Check bottomleft
            potential_moves = []
            row_i = row
            col_i = col
            while ((row_i + 1 < self.ROWS) and (col_i - 1 != -1) and
                   (self.tiles.tiles[row_i+1][col_i-1]) and
                   (self.tiles.tiles[row_i+1][col_i-1].color != color)):
                potential_moves.append((row_i+1, col_i-1))
                row_i += 1
                col_i -= 1

            if ((potential_moves) and
               (row_i + 1 < self.ROWS) and (col_i - 1 != -1) and
               (self.tiles.tiles[row_i+1][col_i-1]) and
               (self.tiles.tiles[row_i+1][col_i-1].color == color)):
                legal_moves["bottomleft"] = potential_moves
                row_i += 1
                col_i -= 1

            # Check bottomright
            potential_moves = []
            row_i = row
            col_i = col
            while ((row_i + 1 < self.ROWS) and (col_i + 1 < self.COLS) and
                   (self.tiles.tiles[row_i+1][col_i+1]) and
                   (self.tiles.tiles[row_i+1][col_i+1].color != color)):
                potential_moves.append((row_i+1, col_i+1))
                row_i += 1
                col_i += 1

            if ((potential_moves) and
               (row_i + 1 < self.ROWS) and (col_i + 1 < self.COLS) and
               (self.tiles.tiles[row_i+1][col_i+1]) and
               (self.tiles.tiles[row_i+1][col_i+1].color == color)):
                legal_moves["bottomright"] = potential_moves
                row_i += 1
                col_i += 1

            # Check topright
            potential_moves = []
            row_i = row
            col_i = col
            while ((row_i - 1 != -1) and (col_i + 1 < self.COLS) and
                   (self.tiles.tiles[row_i-1][col_i+1]) and
                   (self.tiles.tiles[row_i-1][col_i+1].color != color)):
                potential_moves.append((row_i-1, col_i+1))
                row_i -= 1
                col_i += 1

            if ((potential_moves) and
               (row_i - 1 != -1) and (col_i + 1 < self.COLS) and
               (self.tiles.tiles[row_i-1][col_i+1]) and
               (self.tiles.tiles[row_i-1][col_i+1].color == color)):
                row_i -= 1
                col_i += 1
                legal_moves["topright"] = potential_moves

            return legal_moves
