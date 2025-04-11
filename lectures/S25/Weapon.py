from dataclasses import dataclass
import random

@dataclass
class Weapon:
    name: str
    damage: int       # max damage it can do
    durability: int   # how many times you can use it before it breaks

    # Pick a random amount of damage and decrease the durability
    def use(self) -> int:
        self.durability -= 1
        critical_hit = (random.randint(1,12) == 12)

        if critical_hit:
            return 2 * self.damage
        else:
            return random.randint(1, self.damage)

    def is_broken(self) -> bool:
        return self.durability <= 0

    def display(self) -> str:
        return f'{self.name} ({self.damage})'

def random_weapon(cur_round: int) -> Weapon:
    dmg = random.randint(1, cur_round)
    dur = random.randint(1, cur_round)
    adjectives = "big enchanted dragon small wobbly brittle blazing indestructible cursed".split()
    weapons = "sword bow axe staff spear nunchucks slingshot scissors toothpick".split()
    name = random.choice(adjectives) + " " + random.choice(weapons)

    return Weapon(name, dmg, dur)