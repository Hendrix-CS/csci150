from dataclasses import dataclass
from Weapon import *
import random

@dataclass
class Character:
    health: int
    name: str
    specialty: str
    weapon: Weapon

    def display(self) -> str:
        return f'{self.name} ({self.specialty}, {self.health})'

    def set_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def heal(self, hp: int):
        self.health += hp

    def attack(self, other: 'Character') -> int:
        dmg = random.randint(1, self.weapon.damage)
        other.health -= dmg

        return dmg

    def is_dead(self) -> bool:
        return self.health <= 0

def random_monster(round: int) -> Character:
    hp = random.randint(1, round)

    adjectives = "enraged disgraced sad freaky evil".split()
    nouns = "Bill professor ogre Robert banshee EvilGuy".split()

    specialties = "healer berserker drainer murderer".split()

    name = random.choice(adjectives) + " " + random.choice(nouns)
    return Character(hp, name, random.choice(specialties), random_weapon(round))