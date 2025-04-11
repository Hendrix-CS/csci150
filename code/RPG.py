from dataclasses import dataclass
import random

@dataclass
class Weapon:
    name: str
    damage: int

    def get_damage(self) -> int:
        return random.randint(0, self.damage)

    def display(self) -> str:
        return f'{self.name} ({self.damage})'

@dataclass
class Character:
    name: str
    hp: int
    weapon: Weapon

    def attack(self, other: 'Character') -> int:
        dmg = random.randint(0, self.weapon.damage)
        other.take_damage(dmg)
        return dmg

    def take_damage(self, d: int):
        self.hp -= d

    def heal(self, hp: int):
        self.hp += hp

    def is_dead(self) -> bool:
        return self.hp <= 0

    def display(self) -> str:
        return f'{self.name} (HP: {self.hp})'

    def pick_up(self, weapon: Weapon):
        self.weapon = weapon

def print_stats(player, cur_round):
    print('-' * 60)
    print(f'Current round: {cur_round}')
    print(f'HP: {player.hp}')
    print(f'Weapon: {player.weapon.display()}')

def random_weapon(cur_round: int) -> Weapon:
    d = random.randint(1, cur_round)
    adjectives = "enchanted small big green".split()
    weapon_type = "sword spear gun mace".split()
    name = random.choice(adjectives) + " " + random.choice(weapon_type)

    return Weapon(name, d)

def random_enemy(cur_round: int) -> Character:
    dmg = random.randint(1, cur_round)
    hp = random.randint(1, cur_round)
    adjectives = "vicious persnickety snivelling lesser greater".split()
    types = "troll gnome vampire bat wombat".split()
    weapon = "claws dagger poison spell".split()
    name = (random.choice(adjectives) + " " + random.choice(types)).title()

    return Character(name, hp, Weapon(random.choice(weapon), dmg))

def articleize(noun: str) -> str:
    if noun[0] in "aeiou":
        return "an " + noun
    else:
        return "a " + noun

def fight(player, enemy) -> bool:
    fighting = True
    while fighting:
        dmg = player.attack(enemy)
        if dmg == 0:
            print(f'You swing at the {enemy.name} with your {player.weapon.name} but you missed!')
        else:
            print(f'You hit the {enemy.name} with your {player.weapon.name} for {dmg} damage!')
        if enemy.is_dead():
            print('It died!')
            return True

        dmg = enemy.attack(player)
        if dmg == 0:
            print('It missed!')
        else:
            print(f'It hits you with its {enemy.weapon.name} for {dmg} damage!')
        if player.is_dead():
            print('You died!')
            return False

def main():
    name = input("Welcome, adventurer!  What is your name? ")

    player = Character(name, 10, Weapon("rock", 1))

    input(f"Welcome, {name}!  Hit Enter when you're ready to start!")

    keep_playing: bool = True
    cur_round: int = 0
    while keep_playing:
        cur_round += 1

        print_stats(player, cur_round)

        encounter_type = random.randint(1,4)
        if encounter_type == 1:
            weapon = random_weapon(cur_round)
            print(f"You find {articleize(weapon.display())}!")
            if weapon.damage > player.weapon.damage:
                print(f"You throw away your {player.weapon.display()} and pick it up!")
                player.pick_up(weapon)
            else:
                print(f"You decide to keep your {player.weapon.display()}.")

        elif encounter_type == 2:
            enemy = random_enemy(cur_round)
            print(f"A {enemy.display()} appears!")
            keep_playing = fight(player, enemy)

        elif encounter_type == 3:
            potion = random.randint(1, cur_round)
            print(f"You find a health potion. It increases your HP by {potion}!")
            player.heal(potion)

        else:
            print("Nothing happens.")

        print()
        if keep_playing:
            input("Hit Enter when you're ready for the next round.")
        else:
            print(f"Sorry, better luck next time!  You survived for {cur_round} rounds!")

if __name__ == "__main__":
    main()
