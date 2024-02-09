# We cannot prove that this always terminates, but every value
# we have ever checked does terminate. Collatz Conjecture

n = int(input("Give me a positive integer: "))
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)