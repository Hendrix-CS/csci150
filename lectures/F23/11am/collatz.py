
n = 27
count = 0
while n != 1:
    if n % 2 == 0:   # n is even
        n = n // 2
    else:
        n = 3*n + 1
    count = count + 1
    print(n)

print(f'Done!  It took {count} steps to reach 1.')

