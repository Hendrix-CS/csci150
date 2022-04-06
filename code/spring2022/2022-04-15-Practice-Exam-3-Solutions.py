from typing import *

# This fine contains sample solutions to Practice Exam #3. We will spend some time
# in class on 4/15 going over them; for most problems, it is possible that there are other
# ways than those shown here to solve the problem. If you are not sure if your method works, ask!

######################################
# IN - CLASS ###
######################################

# Tracing -- the tracing problems are solved separately, and their solutions are in a pdf on the Webapge

#4

def str_dictionary(s: str) -> Dict[str, int]:
    return_dict = {}
    for char in s:
        if char not in return_dict:
            return_dict[char] = 0
        return_dict[char] += 1

    return return_dict


#5

class CokeBottle:

    def __init__(self):
        self.open = False
        self.amount = 20

    def drink(self, n: int):
        if not self.open:
            print('You cannot drink from a closed bottle.')
        elif self.amount == 0:
            print('You cannot drink from an empty bottle.')
        else:
            self.amount -= n
            if self.amount < 0:
                self.amount = 0

    def toggle_cap(self):
        self.open = not self.open



############################################################
###  TAKE - HOME
###########################################################

#6

def in_order(s: str) -> bool:
    for i in range(1,len(s)):
        if s[i] < s[i-1]:
            return False
    return True

# Two hints on #6 -- you have to use either a while loop or a for loop over range
# You either start at i = 1 and to up to len(s), or start at i = 0 and go to len(s) - 1
# ALso, if you ever find a time you are out of order, you can immediately return False
# Otherwise, you made it all the way through and should return True

#7

def word_hist(s: str) -> Dict[str, int]:
    word_dict = {}
    word_list = s.lower().split(' ')  # this is how you separate word by word
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        if word == 'lemurs':
            word_dict[word] += 3
        else:
            word_dict[word] += 1

    return word_dict


#8

def pref_dict(lst: List[str], n: int) -> Dict[str, int]:
    return_dict = {}
    for word in lst:
        pref = word[0:n]
        if pref not in return_dict:
            return_dict[pref] = 0

    return_dict[pref] += 1

#9

class Animal:

    def __init__(self, color: str, size: int):
        self.color = color
        self.size = size

    def grow(self, n: int):
        self.size += n
        if self.size < 1:
            self.size = 1


    def is_friendly(self) -> bool: # note you do not need to pass size or color as parameters, since 'self' already knows this info
        if self.color == 'red':
            return False
        elif self.size <= 15:
            return True
        elif self.size <=35 and (self.color == 'pruple' or self.color == 'green'):
            return True
        else:
            return False





# 10
class Character:

    def __init__(self):
        self.energy = 20
        self.dist = 0

    def walk(self, n: int):
        if n <= self.energy:
            self.dist += n
            self.energy -= n
        else:
            self.dist += self.energy
            self.energy = 0

    def run(self, n: int):
        if 3 * n <=  self.energy:
            self.dist += n
            self.energy -= 3 * n

        else:
            self.dist += self.energy // 3
            self.energy = self.energy % 3

    def eat(self,n: int):
        self.energy += n

    def rest(self):
        self.energy += 5

