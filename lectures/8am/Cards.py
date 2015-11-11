# Goal: Blackjack

# Today: Playing cards & decks

import random

class Card:

    # Variables:
    #   - suit   (string)
    #   - rank   (string)
    #   - face_up (boolean)

    # Methods:
    #   - __init__(suit, rank)
    #   - get_suit()
    #   - get_rank()
    #   - is_face_up()
    #   - turn()

    def __init__(self, rank, suit):
        """Create a new face-up card with
        the given rank and suit.
        """
        self.suit = suit
        self.rank = rank
        self.face_up = True

    # Three "getter" methods

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def is_face_up(self):
        return self.face_up

    def turn(self):
        self.face_up = not self.face_up

    # Generate a string representation of an object
    # Gets called when you print something
    def __repr__(self):
        if self.face_up:
            return self.rank + self.suit
        else:
            return '**'

class Deck:
    # Variables:
    #   - cards  (list of Cards)
    #
    # Methods:
    #   - __init__()  - make a new deck
    #   - __repr__()
    #   - shuffle()
    #   - sort()
    #   - draw()     - take 1 card
    #   - deal(n)    - take n cards

    def __init__(self):
        self.cards = []
        for suit in ["S","H","D","C"]:
            for rank in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
                c = Card(rank,suit)
                self.cards.append(c)

    def __repr__(self):
        result = ""
        for c in self.cards:
            result += str(c) + " "
        return result

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        """Return the top card from the deck, and remove
        it from the deck."""
        # c = self.cards[0]
        # del self.cards[0]
        c = self.cards.pop(0)
        return c

def main():
    d = Deck()
    d.shuffle()
    print d
    print d.draw()
    print d.draw()
    print d.draw()
    print d

main()
