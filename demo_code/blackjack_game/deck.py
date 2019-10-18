from random import shuffle
from card import Card


class Deck:
    """A deck of cards"""
    def __init__(self):
        suits = ["hearts", "spades", "diamonds", "clubs"]
        values = ["ace", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "jack", "queen", "king"]
        self.cards = [Card(suit, value)
                      for suit in suits
                      for value in values]
        shuffle(self.cards)

    def deal_one(self):
        """Deals one card from the deck"""
        return self.cards.pop()
