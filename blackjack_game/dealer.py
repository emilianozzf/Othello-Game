from deck import Deck
import random as r


class Dealer:
    """
    A blackjack dealer
    """
    def __init__(self):
        DEALER_RANGE = (17, 21)
        self.score = r.randint(*DEALER_RANGE)
        self.deck = Deck()

    def deal_one(self):
        return self.deck.deal_one()
