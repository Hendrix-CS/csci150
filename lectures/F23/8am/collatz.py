
start_num = 1
while start_num <= 1000:
    n = start_num
    num_steps = 0
    while n != 1:
        if n % 2 == 0:  # if n is even
            n = n // 2
        else:
            n = 3*n + 1

        num_steps = num_steps + 1

    print(f"{start_num} {num_steps}")
    start_num = start_num + 1
