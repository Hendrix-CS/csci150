# Collatz conjecture!

n = int(input('What number would you like to start with? '))
count = 0
while n != 1:
    if n % 2 == 0:    # n is even, i.e. remainder when div by 2 is 0
        n = n // 2
    else:
        n = 3 * n + 1
    count = count + 1

print(f"done! It took {count} iterations!")