from Card import *
import random

class Deck:

    # Variables:
    # - list of cards: List[Card]

    # Methods:

    # Create a standard 52-card deck
    def __init__(self, is_empty: bool):
        self.cards = []
        if not is_empty:
            for suit in ['S', 'H', 'D', 'C']:
                for rank in range(1,14):
                    self.cards.append(Card(rank, suit))

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    # Deal cards from the top (end) of the deck into another deck.
    def deal(self, num_cards: int, other_deck: 'Deck'):
        for _ in range(num_cards):
            if (len(self.cards) > 0):
                other_deck.add_card(self.cards.pop())

    def flip_up(self):
        for card in self.cards:
            card.flip_up()

    def flip_down(self):
        pass

    # Add a new card to the top (end) of the deck
    def add_card(self, new_card: Card):
        self.cards.append(new_card)

    def total_blackjack_value(self):
        pass

    def is_blackjack(self):
        pass
