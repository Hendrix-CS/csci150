############# Collatz #################

# Pick a number n
# repeat until n = 1:
#   if n is even, divide it by 2
#   otherwise, multiply by 3 and add 1

# max_n = int(input("Test up to: "))

cur_n = 1
max_steps = 0   # max_steps = largest # of steps to reach 1 seen so far
max_steps_n = 0  # starting number which resulted in the record # of steps
while True:      #cur_n <= max_n:
    # if cur_n % 10000 == 0:
    #     print(cur_n)
    steps = 0
    n = cur_n
    while n > 1:
        steps = steps + 1  # or   steps += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    # Update max_steps if steps is bigger than anything we've
    # seen so far
    if steps > max_steps:
        max_steps = steps
        max_steps_n = cur_n
        print(f"New record: {cur_n} takes {steps} steps.")

    # print(f'{cur_n}: {steps}')

    cur_n += 1

print(f'Record was {max_steps_n}, which took {max_steps} steps')
