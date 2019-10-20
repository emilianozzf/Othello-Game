from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
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
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    team.show_roster()


def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    if team.is_position_filled(position):
        print("Yes, the", position, "position is filled")
    else:
        print("No, the", position, "position is not filled")


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    for player in team.players:
        if player.name == name:
            bench.send_to_bench(name)
            print("Sent", name, "to bench.")
            return
    print(name, "isn't on the team.")


def do_get_player_from_bench(bench):
    if bench.players:
        print("Got", bench.get_from_bench(), "from bench")
    else:
        print("The bench is empty.")


def do_cut_player(team, bench):
    name = input("Who do you want to cut?\n")
    if name in bench.players:
        print(name, "is on the bench, so you cannot cut him!")
    else:
        team.cut_player(name)


def do_show_bench(bench):
    bench.show_bench()


def do_not_understand():
    print("I didn't understand that command")


main()
