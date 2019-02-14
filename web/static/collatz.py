
n: int = int(input("What number do you want to start with? "))

count: int = 0

# Keep going until we reach 1, and count the number
# of loops
while n != 1:
    print(n)
    count = count + 1
    if n % 2 == 0:   # n is even
        n = n // 2
    else:
        n = 3*n + 1

print("Your number needed " + str(count) + " iterations to reach 1.")