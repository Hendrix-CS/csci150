# Do one iteration of the Collatz function
def collatz(n: int) -> int:
    if n % 2 == 0:   # if n is even
        return n // 2
    else:
        return 3*n + 1

# Count how many iterations a starting number takes to reach 1
def collatz_iterations(n: int) -> int:
    count = 0
    while n != 1:
        n = collatz(n)
        count += 1    # abbreviation for count = count + 1

    return count