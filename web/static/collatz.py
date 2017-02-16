# Testing the Collatz Conjecture

# Input: n (int)
# Output: one hailstone step applied to n
def hailstone(n):
    if n % 2 == 0:    #  n % d  is "n mod d" -- remainder when
                               #  n is divided by d.
        return n // 2
    else:
        return 3*n + 1

# Input: n (int)
# Output: number of hailstone iterations needed to reach 1.
def collatz(n):
    count = 0
    while n != 1:
        count = count + 1
        n = hailstone(n)
    return count
