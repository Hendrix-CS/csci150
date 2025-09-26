
# Carry out one step of the hailstone sequence: even -> /2, odd -> *3 + 1
def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

# Take a starting number and repeatedly apply the hailstone function
# until reaching 1, return the number of steps taken.
def hailstone_length(n: int) -> int:
    steps = 0
    while n != 1:
        steps += 1
        n = hailstone(n)

    return steps

# Try all the starting numbers from 1 up to max,
# and print out each number that takes a record number of steps (i.e. more steps than any previous number).
def hailstone_records(max: int):
    n = 1
    record_steps = 0
    while n <= max:
        steps = hailstone_length(n)
        if steps > record_steps:
            record_steps = steps
            print(f'{n} took {steps} steps')

        n += 1