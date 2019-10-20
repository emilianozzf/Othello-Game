class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.players = []

    def send_to_bench(self, player_name):
        self.players.insert(0, player_name)

    def get_from_bench(self):
        return self.players.pop()

    def show_bench(self):
        print("The bench currently includes:")
        if self.players:
            for player in self.players:
                print(player)
        else:
            print("The bench is empty.")
