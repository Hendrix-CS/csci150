from Player import *

from typing import *

def main():
    deck = Deck(False)  # make a standard deck
    deck.shuffle()

    players = [Player("Jack", False), Player("Black", True)]

    blackjack_round(players, deck)

def show_cards(player: Player):
    if player.is_human():
        player.get_hand().flip_up()
    print(player.get_hand())


def blackjack_round(players: List[Player], deck: Deck):
    deal_cards(players, deck)
    for player in players:
        print(player.get_name() + "'s turn!")
        show_cards(player)

        while not player.busted() and player.hit():
            deck.deal(1,player.get_hand())
            show_cards(player)

        if player.busted():
            print("You busted!!!")
            show_cards(player)

def deal_cards(players: List[Player], deck: Deck):
    for player in players:
        # Deal one face down
        deck.deal(1, player.get_hand())
           # Note deck.deal(2,player) would also work,
           # because Player has an add_card method, just like Deck

        # ... and one face up.
        deck.deal(1, player.get_hand(), True)

main()