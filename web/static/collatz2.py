
start: int = 1
while start <= 10000:

    count: int = 0
    n: int = start

    # Keep going until we reach 1, and count the number
    # of loops
    while n != 1:
        count = count + 1
        if n % 2 == 0:   # n is even
            n = n // 2
        else:
            n = 3*n + 1

    print(str(start) + ": " + str(count))

    start = start + 1

