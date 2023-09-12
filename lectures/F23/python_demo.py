# .py files store Python code!

def c_to_f(celsius: float) -> float:
    return 9/5 * celsius + 32

# The special 'print' function prints things on the screen.
print(c_to_f(32))
print('Hello, CSCI 150!')

# The special 'input' function prints a prompt, then waits
# for the user to type something, and returns whatever they
# type as a str.
name: str = input('What is your name? ')
# The int(...) function tries to turn things into an int.
age: int = int(input('Please type your age: '))

# f-strings start with f right before the opening quote mark
# anything inside curly braces has its value printed out.
print(f'Greetings, {name}!')
if age < 20:
    print(f"{age}? That's pretty young.")
elif age < 45:
    print(f'{age} sounds like a good age.')
else:
    print(f"{age}! Wow, you're old.")

print(f'In 10 years you will be {age + 10}.')