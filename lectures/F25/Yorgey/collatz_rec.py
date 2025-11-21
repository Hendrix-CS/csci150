step_dict = {1: 0}

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

# How many steps does n take to reach 1 under the Collatz iteration?
def hailstone_length(n: int) -> int:
    if n not in step_dict:
        step_dict[n] = hailstone_length(hailstone(n)) + 1
    return step_dict[n]

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