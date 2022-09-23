# Some facts about functions:
# - From now on, all of our code will go in functions!
# - To call (use) a function, you must put parentheses after the function name.
#    e.g.   my_function()
#           my_function(6, "hi")
# - The inputs to a function in its definition are called *parameters*.
# - The specific inputs that we give to a function when calling it are *arguments*.
#    e.g.
#      def my_function(x: int, name: str):    <---- x and name are parameters
#
#      ... my_function(6, "hi")   <---- 6 and "hi" are arguments.
# - Any variables defined inside a function are *local* to that function,
#   that is, they only exist inside that function.
#
# e.g.
#
# def my_function():
#     x: int = 6
#     y: str = "hi"
#     ...
#
# def other_function():
#     print(x)             <--- not allowed: x is only defined inside my_function
#

def f(x: int):
    g(x)
    g(x + 2)
    print(x)

def g(z: int):
    z = z*3
    print(z)

def q():
    f(12)
    f(9)

q()