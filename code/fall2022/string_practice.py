# Define the function explode.
# explode(s) should print each character of the string s on a separate line.
# e.g.  explode("hell0")  should print
#   h
#   e
#   l
#   l
#   0

def explode(s: str):
    p: int = 0
    while p < len(s):
        print(s[p])
        p += 1

# sumUpTo(n) should return the sum 1 + 2 + 3 + ... + n.
# e.g.  sumUpTo(3) == 6
def sumUpTo(n: int) -> int:
    k: int = 1
    sum: int = 0
    while k <= n:
        sum += k
        k += 1

    return sum

# Recall the int_input function.
# Should prompt the user with the given prompt,
#   then keep prompting them until they enter a valid int, and return it.
def int_input(prompt: str) -> int:
    valid: bool = False
    while not valid:
        user_input: str = input(prompt)
        if user_input.isdigit():
            valid = True
        elif user_input[0] == '-' and user_input[1:].isdigit():
            valid = True
        else:
            print("Not a valid number, try again.")

    return int(user_input)