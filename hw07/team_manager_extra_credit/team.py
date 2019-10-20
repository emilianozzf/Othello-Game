from player import Player


class Team:
    """A class representing a dodgeball team"""
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

    def is_position_filled(self, position):
        for player in self.players:
            if player.position == position:
                return True
        return False

    def show_roster(self):
        FIRST_LENGTH = 9
        SECONDE_LENGTH = 16
        SPACE = " "
        print("The lineup for", self.name, "is:")
        if self.players:
            for player in self.players:
                print(player.number +
                      (FIRST_LENGTH - len(player.number))*SPACE +
                      player.name +
                      (SECONDE_LENGTH - len(player.name))*SPACE +
                      player.position)
        else:
            print("The team currently has no players")
