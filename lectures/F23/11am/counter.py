
class Counter:

    def __init__(self, upper_bound: int):
        self.upper_bound = upper_bound
        self.count = 0

    def get_count(self):
        return self.count

    def add(self, n: int):
        self.count += n

        # prevent the count from going over the upper bound
        if self.count > self.upper_bound:
            self.count = self.upper_bound

        # You can also do this in one line with the min() function

    def reset(self):
        self.count = 0
