############# Collatz ################3

# Pick a number n
# repeat until n = 1:
#   if n is even, divide it by 2
#   otherwise, multiply by 3 and add 1

n = 27
steps = 0
while n > 1:
    print(n)
    steps = steps + 1
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

print(f'It took {steps} steps')