# Collatz/hailstone conjecture

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


# Set starting number
n: int = 27
# Keep track of number of steps
steps: int = 0
while n != 1:
    steps += 1
    n = hailstone(n)

print(f"Done! It took {steps} steps!")