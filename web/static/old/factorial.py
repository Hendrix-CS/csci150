# Recall n! (n factorial) = 1 * 2 * 3 * ... * n

def factorial_while(n: int) -> int:
    factorial_n = 1
    count = 1
    while count <= n:
        factorial_n *= count
        count += 1
    return factorial_n

# With a for loop?
def factorial_for(n: int) -> int:
    factorial_n = 1
    for i in range(1,n+1):
        factorial_n *= i
    return factorial_n

# n! = n * (n-1) * (n-2) * ... * 1
#    = n * (n-1)!

# We could take this as a *definition* of n!:
#   0! = 1
#   n! = n * (n-1)!   when n > 0.
def factorial_rec(n: int) -> int:
    if n == 0:
        return 1
    else:
        factorial_n = n * factorial_rec(n-1)
        return factorial_n
