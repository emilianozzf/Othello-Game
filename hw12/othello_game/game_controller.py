class GameController:
    """Maintain the state of the game"""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player1_turn = True
        self.player1_no_legal_moves_left = False
        self.player2_no_legal_moves_left = False
        self.game_over = False
        self.player1_score = 2
        self.player2_score = 2

    def update(self):
        """Carry out necessary updates per-frame"""
        if self.player1_turn and self.player1_no_legal_moves_left:
            self.player1_turn = not self.player1_turn

        if (not self.player1_turn) and (self.player2_no_legal_moves_left):
            self.player1_turn = not self.player1_turn

        if self.game_over:
            fill(0.7, 0.5, 0.2)
            textSize(50)
            if self.player1_score == self.player2_score:
                text("PLAYERS TIE", self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.player1_score > self.player2_score:
                text("PLAYER1 WIN", self.WIDTH/2 - 140, self.HEIGHT/2)
            else:
                text("COMPUTER WIN", self.WIDTH/2 - 140, self.HEIGHT/2)
            text("PLAYER1: " + str(self.player1_score),
                 self.WIDTH/2 - 130, self.HEIGHT/2 + 60)
            text("COMPUTER: " + str(self.player2_score),
                 self.WIDTH/2 - 130, self.HEIGHT/2 + 120)
