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

    def __lt__(self, other):
        rank_list = "A23456789TJQK"

        """Return True if self < other, and False otherwise."""
        if (self.suit > other.suit):
            return True
        elif (self.suit < other.suit):
            return False
        else:
            return (rank_list.index(self.rank) < rank_list.index(other.rank))

    # We should really also implement
    #   __le__
    #   __gt__
    #   __ge__
    #   __eq__
    #   __ne__

    def value(self):
        if (self.rank.isdigit()):
            return int(self.rank)
        elif self.rank == 'A':
            return 11
        else:
            return 10

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
    #   - add(c)     - add a card to the top of the deck

    def __init__(self):
        self.cards = []
        for suit in ["S","H","D","C"]:
            for rank in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
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

    def add(self, c):
        """Add the card c to the top of the deck."""
        self.cards.insert(0,c)

    def deal(self, n):
        """Return the top n cards from the deck in a list, and
        remove them from the deck."""

        dealt_cards = []
        for i in range(n):
            dealt_cards.append(self.draw())

        return dealt_cards

    def sort(self):
        # Want to call Python sort() method
        # But we need to tell it what order cards should go in!
        # Implement the __lt__ method in Card

        self.cards.sort()

# More classes:
#   - Hand
#   - Player

class Hand(Deck):
    #  "Hand is-a Deck"  aka  "Hand is a subclass of Deck"
    #  aka "Hand is a more specific kind of Deck"
    #  Hand has everything a Deck has, plus some more specific stuff

    def __init__(self, cards):
        self.cards = cards

    def reveal(self):
        for c in self.cards:
            if not c.is_face_up():
                c.turn()

    def value(self):
        total = 0
        for c in self.cards:
            total += c.value()
        return total

class Player:
    # Variables:
    #
    #   - hand    (Hand)
    #   - name    (string)
    #   - money   (int - number of cents)
    #
    # Methods:
    #
    #   - add_card(c)
    #   - hit_or_stay   - returns true or false
    #   - value         - returns int
    #   - busted        - true/false

    def __init__(self, name):
        self.name = name
        self.hand = Hand([])

    def add_card(self, c):
        self.hand.add(c)

    def add_cards(self, cs):
        for c in cs:
            self.add_card(c)

    def value(self):
        return self.hand.value()

    def busted(self):
        return self.hand.value() > 21

    def __repr__(self):
        return self.name + ": " + str(self.hand)

    # Every player has a hit_or_stay
    #   method but should redefine
    #   ("override") it
    def hit_or_stay(self):
        pass


class HumanPlayer(Player):

    # Override hit_or_stay from Player
    def hit_or_stay(self):
        response = raw_input(self.name + ", hit or stay? ")
        return response.upper() == "HIT"

class ComputerPlayer(Player):

    def hit_or_stay(self):
        return self.hand.value() < 17

############################################################

def one_player(deck, player):

    print player
    hit = player.hit_or_stay()

    while hit and not player.busted():
        player.add_card(deck.draw())
        print player

        if not player.busted():
            hit = player.hit_or_stay()

def blackjack(deck, dealer, player):
    dealer.add_cards(deck.deal(2))
    player.add_cards(deck.deal(2))

    one_player(deck, dealer)
    if (dealer.busted()):
        print "Dealer busted, you win!"
    else:
        one_player(deck, player)

        if (player.busted()):
            print "BUSTED, you lose!"
        else:
            if (player.value() > dealer.value()):
                print "You win!"
            else:
                print "You lose!"

def main():
    d = Deck()
    d.shuffle()

    dealer = ComputerPlayer("ROBOT")
    player = HumanPlayer("You")

    blackjack(d, dealer, player)

main()
