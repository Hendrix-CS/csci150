from Deck import *


class Player:
    # Variables:
    # - name: str
    # - is_human: bool
    # - hand: Deck
    # - money: int

    def __init__(self, name: str, human: bool):
        self.name = name
        self.human = human
        self.hand = Deck(True)

    def __repr__(self):
        return self.name + ": " + str(self.hand)

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def is_human(self):
        return self.human

    # Add a new card to the player's hand
    def add_card(self, new_card: Card):
        self.hand.add_card(new_card)

    # Decide whether to hit (true) or stay (false)
    def hit(self):
        if self.human:
            answer = input("Hit or stay? ")
            return answer == 'hit'
        else:
            return self.hand.total_blackjack_value() < 15

    def busted(self):
        return self.hand.total_blackjack_value() > 21
