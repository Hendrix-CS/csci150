# Count how many iterations a starting number takes to reach 1
def collatz_iterations(n: int) -> int:
    count = 0
    while n != 1:
        n = collatz(n)
        count += 1    # abbreviation for count = count + 1

    return count

# This wouldn't work because collatz is not defined yet
# print(collatz_iterations(5))

# Do one iteration of the Collatz function.
# n is called a "parameter".
def collatz(n: int) -> int:
    if n % 2 == 0:   # if n is even
        return n // 2
    else:
        return 3*n + 1

## More details about functions

# 1. To call/use/execute a function, put parentheses after its name.
# 2. Order of function definitions doesn't matter.
# 3. Inputs in a function's definition are "parameters".
#    Actual inputs given to the function when running it are "arguments".
# 4. Variables defined in a function are "local": they only exist inside
#    the function.

def C_to_F(tempC: float) -> float:
    tempF: float = tempC * 9 / 5 + 32
    return tempF