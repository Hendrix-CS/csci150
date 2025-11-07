from Character import *
from Weapon import *
import random

def main():
    name = input("What is your name, adventurer? ")
    sp = input("What is your specialty? ")

    player = Character(10, name, sp, Weapon("rock", 1))

    round = 0
    while not player.is_dead():
        round += 1
        print(f"Round {round}")
        print(player.display())
        print(player.weapon.display())
        input("Hit Enter when you're ready for the next round!")

        r = random.randint(1, 3)
        if r == 1:
            hp = random.randint(1, round)
            print(f"You found a potion! It increased your health by {hp}.")
            player.heal(hp)
        elif r == 2:
            new_weapon = random_weapon(round)
            print(f"You found a {new_weapon.display()}!")
            if new_weapon.damage > player.weapon.damage:
                print(f"You throw away your {player.weapon.display()} and pick it up!")
                player.set_weapon(new_weapon)
        else:
            monster = random_monster(round)
            print(f'A {monster.display()} appears!')

            while not (monster.is_dead() or player.is_dead()):
                dmg = player.attack(monster)
                print(f"You hit it with your {player.weapon.display()} for {dmg} damage!")
                if monster.is_dead():
                    print("It died!")
                else:
                    dmg = monster.attack(player)
                    print(f"It hits you with its {monster.weapon.display()} for {dmg} damage!")

                    if player.is_dead():
                        print("You died!")


main()