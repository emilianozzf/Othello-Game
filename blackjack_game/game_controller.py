from dealer import Dealer
from hand import Hand


class GameController:
    """
    A controller for a simple blackjack game
    """
    def __init__(self):
        self.BLACKJACK = 21
        self.dealer = Dealer()
        self.player_hand = Hand()

    def start_play(self):
        """
        Starts the game
        """
        print("The dealer's score is", self.dealer.score)
        self.deal_two()
        self.display_hand()
        self.stay_or_hit(input("Would you like to stay or hit?\n"))

    def deal_two(self):
        """
        Deals two cards
        """
        self.player_hand.receive_card(self.dealer.deal_one())
        self.player_hand.receive_card(self.dealer.deal_one())

    def display_hand(self):
        """
        Displays the hand
        """
        self.player_hand.display()

    def stay_or_hit(self, s_or_h):
        """
        Determines whether to stay or hit
        """
        if s_or_h == "hit":
            self.player_hand.receive_card(self.dealer.deal_one())
            self.display_hand()
            if self.player_is_bust():
                self.do_bust()
            else:
                self.stay_or_hit(input("Whoud you like to stay or hit?\n"))
        elif s_or_h == "stay":
            self.do_stay()
        else:
            self.stay_or_hit(input("Whoud you like to stay or hit?\n"))

    def player_is_bust(self):
        """
        Determines if player is bust
        """
        return self.player_hand.score(self.BLACKJACK) > self.BLACKJACK

    def do_stay(self):
        """
        Handles the stay case
        """
        if self.paler_hand.score(self.BLACKJACK) > self.dealer.score:
            print("You win!!")
        elif self.paler_hand.score(self.BLACKJACK) < self.dealer.score:
            print("You lose.")
        else:
            print("you tied.")

    def do_bust(self):
        """Handles bust case"""
        print("**********************")
        print("*        BUST!       *")
        print("**********************")
