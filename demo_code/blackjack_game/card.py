class Card:
    """A playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit

    def num_value(self):
        """Computes the value of the card according to BLACKJACK rules"""
        ACE_VALUE = 11
        FACE_CARD_VALUE = 10
        if self.value == "ace":
            return ACE_VALUE
        elif (self.value == "jack" or
              self.value == "queen" or
              self.value == "king"):
            return FACE_CARD_VALUE
        else:
            return int(self.value)
