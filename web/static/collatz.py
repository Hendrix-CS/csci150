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

# Input: max (int)
# Output: none
#
# Test numbers from 1 up to max and print # of iterations
#  required for each.
def test_collatz(max):
    n = 1
    max_iterations = 0
    max_n = 0
    while True:
        iters = collatz(n)
        if max_iterations < iters:
            max_iterations = iters
            max_n = n
            
            print(str(max_n) + " required " + str(max_iterations) + " iterations.")

        n += 1
