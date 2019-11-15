class GameController:
    """Maintain the state of the game"""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player1_turn = True
        self.players_tie = False
        self.player1_score = 2
        self.player2_score = 2

    def update(self):
        """Carries out necessary actions if players tie"""
        if self.players_tie:
            fill(0.7, 0.5, 0.2)
            textSize(50)
            text("PLAYERS TIE", self.WIDTH/2 - 140, self.HEIGHT/2)
            text("PLAYER1: " + str(self.player1_score),
                 self.WIDTH/2 - 130, self.HEIGHT/2 + 60)
            text("PLAYER2: " + str(self.player2_score),
                 self.WIDTH/2 - 130, self.HEIGHT/2 + 120)
