import math

def print_demo():
    print('Hello, world!')

    print(5)
    print(2.3876)
    print(True)

# format strings (f-strings)

def f_string_demo():
    result = 23

    print('The result is: {result}')   # prints literal string
    print(f'The result is: {result}')  # curly braces have special meaning inside f-string
    print(f'The result is: {result + 7}')

    name = 'Dr. Yorgey'

    print(f'Hi {name}, raw result: {result}; plus 7 is: {result + 7}')

# print: literally puts something on the screen.
# return: specifies the output of a function.

# return is more useful because it lets us use the return value elsewhere
# in our program.
# print ONLY prints something on the screen.
#
# Use return unless you're sure that you want to print.

## input function

# input(prompt) will print out prompt on the screen, then wait for us to
# type something.  Whatever we type will be returned as a string.

def input_demo():
    name = input('What is your name? ')
    print(f'Hello, {name}!')

    answer = input('What is your age? ')  # input ALWAYS returns a string!!
    age = int(answer)  # int(...) tries to convert stuff to an int
    print(f'In 20 years you will be {age + 20}!')

    answer = input('What is your favorite float? ')
    f = float(answer)
    print(f'Your favorite float times pi is {f * math.pi}')

def big_number():
    num = int(input('Enter a number: '))

    # Alternatively:
    # answer = input('Enter a number: ')
    # num = int(answer)

    if num > 100:
        print(f'{num} is a big number!')
    else:
        print(f'{num} is kinda small.')


def get_big_number():
    num = 0
    while num <= 100:
        num = int(input('Enter a number: '))
    return num

# while <condition>:
#     do some stuff
#     do more stuff

# checks the <condition>:
#   - if false, skip the whole while loop
#   - if true, do the stuff inside the while loop, then restart.