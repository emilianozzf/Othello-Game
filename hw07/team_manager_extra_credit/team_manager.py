from team import Team
from bench import Bench


def main():
    # Introduces to the team manager system
    print("Welcome to the team manager.")
    # Creates objects for the team and the bench.
    the_team = Team()
    the_bench = Bench()

    # Interacts with the user until done
    while True:
        # Prompts the user for what he wants to do
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    """
    Sets the team name
    Team -> None
    """
    name = input("What do you want to name the team?\n")
    while not is_alphanumeric(name):
        print("Please enter an alphanumeric team name!")
        name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    """
    Displays the full team roster
    Team -> None
    """
    team.show_roster()


def do_add_player_to_team(team):
    """
    Creates a new player and adds the player to the team
    Team -> None
    """
    player_name = input("What's the player's name?\n")
    while not is_alphanumeric(player_name):
        print("Please enter an alphanumeric player name!")
        player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    while not is_numerical(player_number):
        print("Please enter a numerical player number!")
        player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    while not is_alphanumeric(player_position):
        print("Please enter an alphanumerical player position!")
        player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_check_position_filled(team):
    """
    Determines whether a given position has at least one player filling it,
    then prints the appropriate message
    Team -> None
    """
    position = input("What position are you checking for?\n")
    while not is_alphanumeric(position):
        print("Please enter an alphanumerical position!")
        position = input("What position are you checking for?\n")
    if team.is_position_filled(position):
        print("Yes, the", position, "position is filled")
    else:
        print("No, the", position, "position is not filled")


def do_send_player_to_bench(team, bench):
    """
    Sends an existing player to the bench
    Team Bench -> None
    """
    name = input("Who do you want to send to the bench?\n")
    while not is_alphanumeric(name):
        print("Please enter an alphanumeric name!")
        name = input("Who do you want to send to the bench?\n")
    for player in team.players:
        if player.name == name:
            bench.send_to_bench(name)
            print("Sent", name, "to bench.")
            return
    print(name, "isn't on the team.")


def do_get_player_from_bench(bench):
    """
    Gets the best-rested player by name from the bench (i.e. the player who has
    been on the bench longest)
    Bench -> None
    """
    if bench.players:
        print("Got", bench.get_from_bench(), "from bench")
    else:
        print("The bench is empty.")


def do_cut_player(team, bench):
    """
    Cuts the player
    Team Bench -> None
    """
    name = input("Who do you want to cut?\n")
    while not is_alphanumeric(name):
        print("Please enter an alphanumeric name!")
        name = input("Who do you want to cut?\n")
    if name in bench.players:
        print(name, "is on the bench, so you cannot cut him!")
    else:
        team.cut_player(name)


def do_show_bench(bench):
    """
    Shows the names of the players who are currently on the bench
    Bench -> None
    """
    bench.show_bench()


def do_not_understand():
    """
    Deals with mis-typed command
    None -> None
    """
    print("I didn't understand that command")


def is_numerical(string):
    for c in string:
        if ord(c) not in range(ord('0'), ord('9')+1):
            return False
    return True


def is_alphanumeric(string):
    for c in string:
        if ((ord(c) not in range(ord('a'), ord('z')+1)) and
           (ord(c) not in range(ord('0'), ord('9')+1)) and
           (ord(c) != ord(" "))):
            return False
    return True


main()
