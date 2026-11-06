from dataclasses import dataclass
import random

# Reminders:

# Grade Update emails

#   Quiz today, Dictionaries
#   Final Project Design Document Due Monday, November 16 (2 weeks)
# Homework: Assigned -- Classes


# Deck of Cards

# We want to build a deck of cards
# # --each card has a Suit: Hearts, Diamonds, Spades, Clubs
# # --and a rank, 2, 3, ..., 10, J, Q, K, A

@dataclass
class Card:

    suit: str
    rank: int  # we will use numbers 2 - 14

    def card_value(self) -> int:
        if self.rank <= 10:
            return self.rank
        elif self.rank <=13:
            return 10
        else:
            return 11

    def pretty_card(self)->str:
        if self.rank <= 10:
            pretty_rank = str(self.rank)
        elif self.rank == 11:
            pretty_rank = 'Jack'
        elif self.rank == 12:
            pretty_rank = 'Queen'
        elif self.rank == 13:
            pretty_rank = 'King'
        else:
            pretty_rank = 'Ace'

        return f'{pretty_rank} of {self.suit}'



# What if we want a Player class -- who might have a hand of cards?

@dataclass
class Player:

    hand: list

    def get_card(self, c: 'Card'):
        self.hand.append(c)

    def has_card(self, s: str, r: int) -> bool:
        for c in self.hand:
            if c.suit == s and c.rank == r:
                return True
        return False

    def discard(self, s: str, r: int) -> 'Card':
        for c in self.hand:
            if self.has_card(s,r):
                self.hand.remove(c)
                return c

# And maybe a Deck class
@dataclass
class Deck:

    deck: list

    def build_deck(self):
        for suit in ['H','D','S','C']:
            for rank in range(2,15):
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self) -> 'Card':
        return self.deck.pop(0)




d = Deck([])
d.build_deck()
d.shuffle()
print(d)

a = Player([])
b = Player([])

for i in range(5):
    a.get_card(d.deal())
    b.get_card(d.deal())

print(a)
print(b)