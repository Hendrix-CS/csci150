# This file contains 2 topics:
#
#     * a short introduction to f-strings
#     * tracing, using the function stack -- there are three total examples given
#           and I have separately posted the completed traces on the Team page


# f-strings
# Recall at the end of yesterday's class, we had:
#
#print('The integer ', curr_n, ' takes ', collatz_steps(curr_n), ' steps to reach 1.')
#
# where curr_n and collatz_steps(curr_n) were both integers. Though this works, we can make the ouput better
# by using a f-string (a "formatted string").

x = 5
t = 'hi there'
z = 12.4

#print('I like the number ', x, '. ', t, ' and the number ',z)

#print(f'I like the number {x}. {t} and the number {z}')

# the f-string lets you directly control the format, and you don't have to remember commas, spaces, etc.


# The Function Stack

# The Function Stack is the fundamental way that Python controls which function is being run
# during the execution of a file -- and how it deals with memory issues and variables.

# The stack works in a last-in, first-out mode. That is, the last item added to the stack if the first
# thing that gets processed. Once that happens, the next item is the second to last added, etc.

# Think of it like having a stack of books next to your bed. Every time you buy a new book, it goes on top
# When you read, you read whatever the top book is on the stack. If you finish that book,
# you put it aside and go to the next -- but even if you are in the middle of one
# when you buy a new book, the new book goes on top, and is what you read the next evening.

# Let's look at an example:

# (The completed tracing solutions are all found in the Tracing folder on the Teams page)

# Example 1:


def g(z: int):
    z =  z * 3
    print(z)


def f(x: int):
    g(x)
    g(x + 2)
    print(x)


#f(3)

# Notice that in this first example, neither g or f have explicit return values (print != return)



# Example 2:

def alice(z : int) -> int:
    if z > 0:
        return z * 2
    else:
        return z + 10

def bob(x : int, y : int) -> int:
    if y < x:
        return alice(x) + alice(y)
    else:
        return alice(x + y)

def main2():
    print(bob(6,7))

#main2()

# We then ran example 2.5, which changed main's print line to print(bob(8,-2))

def main25():
    print(bob(8,-2))

#main25()


# Example 3:

def aaa(x: int, s: str) -> int:
    z = 7
    if x < z and s < 'hello':
        z += 3
        print(f'My string is {s} and number is {x}.')
    else:
        z *= 4
        print(f'I do not like the number {x}.')
    return z

def bbb(x: int, y: int) -> int:
    if x < y:
        return y // x
    else:
        return x - y

def main3():
    x = bbb(7,2)
    print(aaa(x,'hi'))
    print(aaa(bbb(3,14),'abcd'))

#main3()

#############################
# We got to here in class
# Please look through the next example before Wednesday and try it on your own
# The solution is posted along with the others on the Team page

# An example with a while loop

#Example 4

def while_ex(n: int) -> int:
    i = 0
    j = 0
    while i < n:
        j += i
        i += 1

    return j

def main4():
    print(while_ex(3))
    print(while_ex(4))

#main4()