from random import randint
from deck import Deck


class Dealer:
    """A blackjack dealer"""
    def __init__(self):
        DEALER_RANGE = (17, 21)
        self.score = randint(*DEALER_RANGE)
        self.deck = Deck()

    def deal_one(self):
        """Deals one card from the dealer"""
        return self.deck.deal_one()
