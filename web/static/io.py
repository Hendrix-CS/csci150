
print('Hello world!')

x: int = 3
print(x)

print('Hello ' + 'again')

# str(x) gives us a string containing the
# formatted value of x
print('The value of x is ' + str(x))

name: str = input('What is your name? ')

print('Hello, ' + name + '!')

favorite_str: str = input('What is your favorite number? ')
favorite: int = int(favorite_str)   # Convert a string to an int

print('Three more than your favorite number is ' + str(favorite + 3) + '.')