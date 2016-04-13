# 11 April 2016
# Blackjack!

import random

class Card:

    # Variables:
    #   - suit (string: S, H, D, C)
    #   - rank (string)
    #   - face_up  (boolean)

    # Other ideas:
    #   - where the card is

    # Functions:
    #   - 3 "getter" methods:
    #     - get_suit()
    #     - get_rank()
    #     - is_face_up()
    #   - Other methods:
    #     - blackjack_value()
    #     - flip()
    #     - __repr__

    # Create a card which is face-down by default.
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = False

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def is_face_up(self):
        return self.face_up

    def flip(self):
        self.face_up = not self.face_up        

    # Returns a string representation of the object
    def __repr__(self):
        if self.face_up:
            return self.rank + self.suit
        else:
            return '**'

    def blackjack_value(self):
        if self.rank == 'A':
            return 1
        elif self.rank.isdigit():
            return int(self.rank)
        else:
            return 10

        # Alternatives:
        # "A23456789TJQK" -- look up index
        # dictionary rank -> value

    # Decide whether one card is less than another.
    def __lt__(self, other):
        # Standard bridge ordering:
        #   A-K S, A-K H, A-K D, A-K C.

        # clever hack: suits happen to be ordered
        #   reverse alphabetically!
        if (self.suit > other.suit):
            return True
        elif (self.suit < other.suit):
            return False
        else:
            # suits are the same
            ranks = "A23456789TJQK"
            return ranks.find(self.rank) < ranks.find(other.rank)

    # Really should also implement:
    # __gt__    (greater)
    # __eq__   (equal)
    # __ge__   (greater or equal)
    # __le__    (less or equal)
    # __ne__   (not equal)
    #
    # But sort() only uses lt.

# A deck is a sequence of cards.
class Deck:

    # Variables:
    #   - cards: list of Card objects.

    # Methods:
    #   - shuffle
    #   - sort
    #   - add_card
    #   - draw: return one card
    #   - deal: return a list of n cards
    #   - deal_hands: return a list of hands

    # Create a standard 52-card deck.
    # suits and ranks are *optional* parameters.
    def __init__(self, suits = "SHDC", ranks = "A23456789TJQK"):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append( Card(rank, suit) )

    def __repr__(self):
        output = ""
        for card in self.cards:
            output += str(card) + " "
        return output

    # Flip all the cards face-up
    def reveal(self):
        for card in self.cards:
            if not card.is_face_up():
                card.flip()

    # Shuffle the cards.
    def shuffle(self):
        random.shuffle(self.cards)

    # Sort the cards.
    def sort(self):
        self.cards.sort()
        # But how does Python know how to sort cards?
        # We need to tell it --- by adding another method
        #   to Card

    # Remove the top (leftmost) card from the deck
    # and return it
    def draw(self):
        return self.cards.pop(0)
        # TODO: fix so this doesn't crash for an empty Deck
        "oierfkjerfh jhesrkfj hser f" +\
        "fkhrkfjehrfe"

        
