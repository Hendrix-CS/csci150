def input_integer(prompt: str) -> int:
    valid = False
    while not valid:
        value = input(prompt)
        if value.isdigit() or value[0] == '-' and value[1:].isdigit():
            valid = True
            value_int = int(value)
        else:
            print("Not a number, try again!")
    return value_int

def get_sum() -> int:
    value1 = input_integer("Enter a number: ")
    value2 = input_integer("Enter another number: ")

    return value1 + value2


def splaz(n: int) -> int:
    counter = 0
    while not (n == 1 or counter >= 100):
    # while n != 1 and counter < 100:      # equivalent
        if n % 3 == 0:
            n //= 3
        else:
            n = 2*n + 1
        counter += 1

    if counter == 100:   #  if n != 1
        return -1
    else:
        return counter












