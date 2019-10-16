class Hand:
    """
    A blackjack hand
    """
    def __init__(self):
        self.cards = []
        self.number_of_aces = 0

    def receive_card(self, card):
        """
        Receives a card
        """
        if card.value == "ace":
            self.number_of_aces += 1
        self.cards.append(card)

    def score(self, BLACKJACK, ):
        """
        Calculates the score
        """
        s = sum([c.num_value() for c in self.cards])
        aces_count = self.number_of_aces
        ACE_REDUCTION = 10
        while s > BLACKJACK:
            if aces_count > 0:
                s -= ACE_REDUCTION
                aces_count -= 1
            else:
                return s
        return s

    def display(self):
        """
        Prints out the hand
        """
        print("Player hand:")
        for c in self.cards:
            print(c)
