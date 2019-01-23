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
    def deal(self, num_cards: int, other_deck: 'Deck', flip : bool = False):
        for _ in range(num_cards):
            if (len(self.cards) > 0):
                card = self.cards.pop()
                if flip:
                    card.flip_up()
                other_deck.add_card(card)

    def flip_up(self):
        for card in self.cards:
            card.flip_up()

    def flip_down(self):
        pass

    # Add a new card to the top (end) of the deck
    def add_card(self, new_card: Card):
        self.cards.append(new_card)

    # Get the total blackjack value of all the cards
    # in the deck.
    def total_blackjack_value(self):
        total = 0
        for card in self.cards:
            total += card.blackjack_value()
        return total

    def is_blackjack(self):
        pass
