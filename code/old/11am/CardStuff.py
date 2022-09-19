from typing import *
import random

class Card:

    def __init__(self, rank:str, suit:str):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def rank_match(self, other:"Card") -> bool:
        return self.rank == other.rank

    def suit_match(self, other:"Card") -> bool:
        return self.suit == other.suit

    def any_match(self, other:"Card") -> bool:
        return self.suit_match(other) or self.rank_match(other)

    def simple_repr(self):
        return self.rank + ":" + self.suit

class Hand:

    def __init__(self):
        self.cards = []

    def show_cards(self) -> str:
        s = ""
        for c in self.cards:
            s += c.simple_repr() + ", "
        return s[:-2]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> "Card":
        return self.cards.pop(0)

    def add_card(self, c: "Card"):
        self.cards.append(c)

    def peek(self) -> "Card":
        return self.cards[-1]

    # https://stackoverflow.com/questions/15114023/using-len-and-def-len-self-to-build-a-class
    def __len__(self) -> int:
        return len(self.cards)

    def matches(self, top: "Card") -> List["Card"]:
        m: List["Card"] = []
        for c in self.cards:
            if c.any_match(top):
                m.append(c)
        return m

    def remove(self, which: "Card"):
        self.cards.remove(which)



class Deck(Hand):

    ranks: List[str] = ["A", "2", "3", "4", "5", "6",
                        "7", "8", "9", "10", "J", "Q", "K"]
    suits: List[str] = ["C", "D", "H", "S"]

    def __init__(self):
        Hand.__init__(self)
        for r in Deck.ranks:
            for s in Deck.suits:
                self.cards.append(Card(r, s))

class Player:

    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()

    def add_card(self, c: "Card"):
        self.hand.add_card(c)

    def show_me(self):
        return f"{self.name}: {self.hand.show_cards()}"

    def is_winner(self) -> bool:
        return len(self.hand) == 0

    def play(self, top: "Card") -> "Card":
        if self.can_play(top):
            m = self.hand.matches(top)
            which = random.choice(m)
            self.hand.remove(which)
            return which
        else:
            return None

    def can_play(self, top: "Card") -> bool:
        m = self.hand.matches(top)
        return len(m) > 0

def test():
    c = Card("2", "H")
    print(c)
    c2 = Card("2", "S")
    print(c.rank_match(c2))
    print(c.suit_match(c2))
    print(c.any_match(c2))

    d = Deck()
    print(d.show_cards())
    d.shuffle()
    print(d.show_cards())

    h = Hand()
    for i in range(5):
        h.add_card(d.deal())
        print(h.show_cards())

    print(h.peek().simple_repr())
    print(h.show_cards())

    p = Player("Random1")
    for i in range(5):
        p.add_card(d.deal())
        print(p.show_me())

    print(p.play(Card("2", "H")))
    print(p.show_me())

    print(d.show_cards())
    print(len(d))

    print(Deck.ranks)


    g = Game()
    count = g.play()


if __name__ == '__main__':
    test()
