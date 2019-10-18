from die import Die


class PairOfDice:
    """A pair of dice"""
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        """Rolls the dice"""
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        """Calculates the current value of dice"""
        return (self.die1.current_value + self.die2.current_value)
