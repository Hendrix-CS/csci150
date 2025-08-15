from dataclasses import dataclass

from Weapon import *

@dataclass
class Character:
    name: str
    hp: int
    weapon: Weapon

    def heal(self, hp: int):
        self.hp += hp

    def attack(self, other: 'Character') -> int:
        dmg = self.weapon.use()
        other.hp -= dmg
        return dmg

    def is_dead(self) -> bool:
        return self.hp <= 0

    def display(self) -> str:
        return f'{self.name} ({self.hp})'

def random_enemy(cur_round: int) -> Character:
    hp = random.randint(1, cur_round)
    adjectives = "enraged magnificent microscopic vicious".split()
    names = "dave cthulhu vampire chicken_jockey newt axolotl goblin IRS_agent".split()
    for i in range(len(names)):
        names[i] = names[i].replace('_', ' ')
    name = random.choice(adjectives) + " " + random.choice(names)
    return Character(name, hp, random_weapon(cur_round))


