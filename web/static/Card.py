class Card:

    # Variables:
    # - suit: str
    # - rank: int
    # - face_up: boolean

    # Don't store color since we can recover it from suit

    # Methods:

    # Create a card which is initially face down
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit
        self.face_up = False

    # Flip the card over
    def flip(self):
        self.face_up = not self.face_up

    def is_face_up(self) -> bool:
        return self.face_up

    def flip_up(self):
        self.face_up = True

    # Get the color of the card
    def get_color(self) -> str:
        if self.suit in ['S','C']:
            return "black"
        else:
            return "red"

    # Get the suit
    def get_suit(self) -> str:
        return self.suit

    # Get the rank
    def get_rank(self) -> int:
        return self.rank

    # Get the value of the card in blackjack
    # Ace = 1, face cards = 10.
    def blackjack_value(self) -> int:
        if self.rank >= 10:
            return 10
        else:
            return self.rank

    def __repr__(self) -> str:
        return self.__str__()
        # return 'Card(' + self.....  + ',' + ...

    # Return a representation of the card as a string,
    # e.g.  '2H', 'QS', 'TC', 'AD'
    def __str__(self) -> str:
        if self.face_up:
            rank_dict = {1:'A',10:'T',11:'J',12:'Q',13:'K'}
            if self.rank in rank_dict:
                return rank_dict[self.rank] + self.suit
            else:
                return str(self.rank) + self.suit
        else:
            return '**'