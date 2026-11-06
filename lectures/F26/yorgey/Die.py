from dataclasses import dataclass
import random

@dataclass
class Die:
    sides: int
    cur_side: int = 0

    def roll(self) -> int:
        self.cur_side = random.randint(1, self.sides)
        return self.cur_side

    def prev_roll(self) -> int:
        return self.cur_side
