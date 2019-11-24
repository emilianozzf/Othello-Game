class Player2:
    """Player2 class"""
    def __init__(self, board, game_controller):
        self.board = board
        self.gc = game_controller

    def move(self):
        """Player2 is computer AI that always chooses the "best" square"""
        legal_move_flips = {}
        for i in range(len(self.board.tiles.tiles)):
            for j in range(len(self.board.tiles.tiles[i])):
                legal_moves = self.board.search_legal_moves(i, j, 1)
                if legal_moves:
                    num_of_flips = 0
                    for direction in legal_moves:
                        num_of_flips += len(legal_moves[direction])
                    legal_move_flips[(i, j)] = num_of_flips

        if legal_move_flips:
            sorted_legal_move_flips = sorted(
                legal_move_flips.items(),
                key=lambda x: x[1],
                reverse=True
            )
            best_move = sorted_legal_move_flips[0][0]
            self.board.put_tile(best_move[1]*100, best_move[0]*100, 1)
