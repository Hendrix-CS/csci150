from Character import *

def main():
    cur_round: int = 0
    name = input("What is your name, adventurer? ")

    player = Character(name, 10, Weapon('rock', 1, 5))

    while not player.is_dead():
        cur_round += 1
        print()
        input("Hit Enter when you're ready for the next round!")
        print("------------------------------------------------")
        print(f'Round {cur_round}')
        print(player.display())
        print(f'Weapon: {player.weapon.display()}')

        n = random.randint(1, 4)
        if n == 1:
            hp = random.randint(1, cur_round)
            print(f'You find a potion! It increases your HP by {hp}!')
            player.heal(hp)
        elif n == 2:
            print("Nothing happens!")
        elif n == 3:
            new_weapon = random_weapon(cur_round)
            print(f'You find a {new_weapon.display()}!')
            if new_weapon.damage > player.weapon.damage:
                print(f'You throw away your {player.weapon.display()} and pick it up!')
                player.weapon = new_weapon
            else:
                print(f'You decide to keep your {player.weapon.display()}.')
        elif n == 4:
            enemy = random_enemy(cur_round)

            print(f'A {enemy.display()} appears!')
            while not (player.is_dead() or enemy.is_dead()):
                dmg = player.attack(enemy)
                print(f'You hit it with your {player.weapon.name} for {dmg} damage!')
                if enemy.is_dead():
                    print('It died!')
                else:
                    dmg = enemy.attack(player)
                    print(f'It hits you with its {enemy.weapon.name} for {dmg} damage!')
                    if player.is_dead():
                        print('You died!')

main()