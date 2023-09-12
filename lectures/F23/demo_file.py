def c_to_f(celsius: float) -> float:
    return celsius * 9/5 + 32

# print is a special function for printing things on the screen
print(c_to_f(32))
print('Hello, "CSCI 150"!')

# input function prints the prompt, waits for the user to type something,
# then returns whatever they type as a str.
name: str = input('Please enter your name: ')
age: int = int(input('Please enter your age: '))

# f-string can be used to format information
print(f"Hello, {name}! Today it is {c_to_f(32)} degrees F.")
if age < 20:
    print(f'{age}? You are very young.')
elif age < 45:
    print(f'{age} sounds perfect')
else:
    print(f'{age}! Wow, you are old.')

print(f'In 10 years, you will be {age + 10}.')