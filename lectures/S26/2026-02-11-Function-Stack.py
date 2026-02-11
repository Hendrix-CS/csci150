# Reminders

# Quiz #2 - Friday (Booleans and Conditionals)
# Homework #3 Assigned (Function Stack)
# Project #1 -- Due in 2 Weeks

# print and input

# We have previously talked about print. One extra thing:
# Format strings!

x = 4
print('My number is ', x)
print(f'My number is {x}')

# In an f-string (format string), you preface with the letter f
# Then make a string and anything in {curly braces} is read as its value
# rather than the literal string.

# Input
y = input('Please enter a number: ')
print(f'You entered the number {y}. Is that correct?')

# Note: input always returns as string!

print(2 + int(y))


###########################
# Back to the function stack.

def aa():
    print('Hello there.')


def bb(x: int) -> int:
    if x > 5:
        aa()
        return x - 9

    else:
        if x == -1:
            aa()
            aa()
            return x - 1
        else:
            return x + 5
            aa()


# main() *NEVER* takes any parameters, and never returns anything
# also, no function *EVER* calls main()

def main():
    x = bb(8)
    y = bb(x)
    z = bb(2)
    print(x + y + z)


main()




############################### Practice Problems from Class

# 1

def g(z: int):
    z =  z * 3
    print(z)


def f(x: int):
    g(x)
    g(x + 2)
    print(x)


f(3)



# 2

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

main2()

#2.5 -- we just change the main()
def main25():
    print(bob(8, -2))

main25()


# 3
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

main3()