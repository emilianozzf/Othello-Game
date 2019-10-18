from pair_of_dice import PairOfDice


class GameController:
    """A controller for a simple dice game"""
    def __init__(self):
        self.FIRST_ROLL_LOSE_VALUES = [2, 3, 12]
        self.FIRST_ROLL_WIN_VALUES = [7, 11]
        self.REMAINING_ROLLS_LOSE_VALUE = 7
        self.pair_of_dice = PairOfDice()
        self.current_value = 0
        self.shooter_point = 0

    def start_play(self):
        """Starts the game"""
        self.roll_dice()
        self.shooter_point = self.pair_of_dice.current_value()
        if self.current_value in self.FIRST_ROLL_LOSE_VALUES:
            print("You rolled " + str(self.current_value) + ". You lose.")
        elif self.current_value in self.FIRST_ROLL_WIN_VALUES:
            print("You rolled " + str(self.current_value) + ". You win!")
        else:
            print("You point is " + str(self.shooter_point))
            self.continue_to_roll()

    def roll_dice(self):
        """Rolls the dice"""
        input("Press enter to roll the dice...\n")
        self.pair_of_dice.roll_dice()
        self.current_value = self.pair_of_dice.current_value()

    def continue_to_roll(self):
        """Continues to roll the dice"""
        self.roll_dice()
        if self.current_value == self.REMAINING_ROLLS_LOSE_VALUE:
            print("You rolled " + str(self.current_value) + ". You lose.")
        elif self.current_value == self.shooter_point:
            print("You rolled " + str(self.current_value) + ". You win!")
        else:
            print("You rolled " + str(self.current_value) + ".")
            self.continue_to_roll()
