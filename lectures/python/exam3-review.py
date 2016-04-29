# Multiplication, recursively

# Input: two nonnegative integers
# Output: x*y
def mul(x, y):
    # Base case: x = 0
    if x == 0:
        return 0
    # Otherwise x is 1 + something
    else:
        return y + mul(x-1, y)

class StoneSoup:
    # Variables:
    #    - tasty_threshold (int)
    #    - ingredient_list (list of strings)

    def __init__(self, num):
        self.tasty_threshold = num
        self.ingredient_list = []

    def add(self, ingredient):
        if ingredient not in self.ingredient_list:
            self.ingredient_list.append(ingredient)

    def tasty(self):
        return (len(self.ingredient_list) >= self.tasty_threshold)
