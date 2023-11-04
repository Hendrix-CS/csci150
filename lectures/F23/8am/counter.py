class Counter:

    def __init__(self, upper_bound: int):
        self.upper_bound: int = upper_bound
        self.count = 0

    def get_count(self):
        return self.count

    def add(self, n: int):
        # Add n but don't go over the upper bound
        # min returns the smaller of the two numbers
        self.count = min(self.upper_bound, self.count + n)

        # Alternatively:
        # self.count += n
        # if self.count > self.upper_bound:
        #    self.count = self.upper_bound

    def inc(self):
        self.add(1)

    def reset(self):
        self.count = 0
