# 11 April 2016
# Blackjack!

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

    

        
