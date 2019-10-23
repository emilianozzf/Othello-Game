from player import Player


class Team:
    """A class representing a dodgeball team"""
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        """Sets the team name"""
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        """Creates a new player object then adds that player object to the
        team's players list"""
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        """Removes the player with the name player_name from the players
        list"""
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

    def is_position_filled(self, position):
        """Checks whether there is currently at least one player on the team
        occupying the requested position"""
        for player in self.players:
            if player.position == position:
                return True
        return False

    def show_roster(self):
        """Displays the full team roster"""
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
