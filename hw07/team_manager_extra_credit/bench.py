class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.players = []

    def send_to_bench(self, player_name):
        """Puts the player onto the bench"""
        self.players.insert(0, player_name)

    def get_from_bench(self):
        """Return the name of the player who has been on the bench longest"""
        return self.players.pop()

    def show_bench(self):
        """Displays the current list of players on the bench"""
        print("The bench currently includes:")
        if self.players:
            for player in self.players:
                print(player)
        else:
            print("The bench is empty.")
