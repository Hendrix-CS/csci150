from dataclasses import dataclass
import random

@dataclass
class Weapon:
    name: str
    damage: int

    def display(self) -> str:
        return f'{self.name} ({self.damage})'

def random_weapon(round: int) -> Weapon:
    adjectives = "flaming sharp dull powerful cursed bent broken".split()
    material = "tungsten wooden steel aluminum glass kryptonite plastic marshmallow".split()
    nouns = "sword axe spear bow dagger scythe cutlass mace pencil stick".split()

    adj = random.choice(adjectives)
    if adj == "powerful":
        dmg = random.randint(round, 2*round)
    else:
        dmg = random.randint(1, round)

    name = adj + " " + random.choice(material) + " " + random.choice(nouns)

    return Weapon(name, dmg)
