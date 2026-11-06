from dataclasses import dataclass
import random
from Die import *

@dataclass
class Pet:
    animal: str
    stats: dict[str, int]

    def display(self) -> str:
        return self.animal + str(self.stats)

def random_pet(max: int) -> Pet:
    animal_list = ["sting ray", "monkey", "marmot", "dog", "lemur", "cat", "chinchilla", "snake", "giraffe", "rock", "unicorn"]
    stats_list = ["strength", "speed", "determination", "confidence", "friendliness", "furriness", "sustainability", "length", "reproducibility", "legs", "colorfulness"]

    animal = random.choice(animal_list)

    stat_choices = random.sample(stats_list, 3)

    d = Die(max)
    stats = {}
    for stat in stat_choices:
        stats[stat] = d.roll()

    return Pet(animal, stats)