from random import randint


class Die:
    """A single die"""
    def __init__(self):
        self.current_value = 0

    def roll(self):
        """Rolls the dice"""
        self.current_value = randint(1, 6)
