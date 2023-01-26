class Character:
    # No parameters to __init__ since all
    # variables are initialized to specific default
    # values
    def __init__(self):
        self.energy: int = 20
        self.dist: int = 0

    def walk(self, n: int):
        if self.energy < n:
            self.dist += self.energy
            self.energy = 0
        else:
            self.dist += n
            self.energy -= n

        # Alternative implementation:
        # move = min(n, self.energy)
        # self.dist += move
        # self.energy -= move

    def run(self, n: int):
        run_so_far = 0
        while self.energy >= 3 and run_so_far < n:
            run_so_far += 1
            self.dist += 1
            self.energy -= 3

    def eat(self, n: int):
        self.energy += n

    def rest(self):
        self.energy += 5

####### 9 ##########################

class Animal:
    def __init__(self, color: str, size: int):
        self.color = color
        self.size = size

    # etc.


###### 8 ############################

from typing import *

def pref_dict(lst: List[str], n: int) -> Dict[str, int]:
    d = {}

    for s in lst:
        prefix = s[0:n]   # get the first n characters
        if prefix in d:
            d[prefix] += 1
        else:
            d[prefix] = 1

        # Alternative:
        # if prefix not in d:
        #     d[prefix] = 0
        # d[prefix] += 1

    return d

###### 6 #############

def in_order(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            return False

    # Alternative
    # i = 0
    # while i < len(s) - 1:
    #     if s[i] > s[i+1]:
    #         return False
    #     i += 1

    return True