# Functions!

# 1. From now on, all your code should go inside functions!
# e.g.
#
# # Test the Collatz conjecture up to a given upper limit.
# def main():
#     limit = int(input("Test numbers up to: "))
#     start = 1
#     while start < limit:
#         n = start
#         count = 0
#         while n != 1:        # keep looping until reaching 1
#             if n % 2 == 0:   # if n is even
#                 n = n // 2
#             else:
#                 n = 3*n + 1
#             count = count + 1
#         print(f'{start}: {count}')
#         start = start + 1
#
# main()

# 2. You should write a comment before every function explaining its inputs, output, and what it does.

# r(z) returns f(z) * f(z+1).
def r(z: int) -> int:
    return f(z) * f(z+1)


# f returns the value 7 greater than its input.
def f(x: int) -> int:
    y = x + 7 / 0
    return y


# g returns the number 2.
def g() -> int:
    return 2

# 3. To run a function, you must put parentheses after its name (with any needed inputs).

# 4. The order of function definitions doesn't matter!

# 5. The inputs in the definition of a function (inside the parentheses) are called "parameters".
#   e.g. in the definition of f above, x is a parameter.
# When we call (use) a function, the inputs we give it are called "arguments".
#   e.g. if I write  f(6),  6 is an argument.

# 6. Parameters and variables defined inside a function are *local*, i.e. they can only be accessed
#    inside the function.

# Python keeps a "stack" (i.e. a pile) of functions which are in the middle of executing.
#   Every time a function calls another function, the first function is paused and put on the top of the stack,
#   then the new function is executed.  When done with one function, Python will pick up executing the
#   one on top of the stack.

# q does something random, we have no idea.
def q(m: int, n: int) -> int:
    var = r(m) + r(n)
    return var

