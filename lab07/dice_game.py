from game_controller import GameController


def main():
    game_controller = GameController()
    print("--------------------------------\n" +
          "Welcome to street craps!\n\n" +
          "Rules:\n" +
          "If you roll 7 or 11 on your first roll, you win.\n" +
          "If you roll 2, 3, or 12 on your first role, you lose.\n" +
          "If you roll anything else, that's your 'point', and\n" +
          "you keep rolling until you either roll your point\n" +
          "again (win) or roll a 7 (lose)\n")
    game_controller.start_play()


main()
