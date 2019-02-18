
def hailstone(m: int) -> int:
    if m % 2 == 0:  # n is even
        m = m // 2
    else:
        m = 3 * m + 1
    return m

def count_iterations(n: int) -> int:

    count: int = 0

    # Keep going until we reach 1, and count the number
    # of loops
    while n != 1:
        count = count + 1
        n = hailstone(n)

    return count

def format_count(start: int, count: int):
    print(str(start) + ": " + str(count))

def test_collatz(high: int):
    start: int = 1
    while start <= high:
        count: int = count_iterations(start)
        format_count(start, count)
        start = start + 1

test_collatz(100)
