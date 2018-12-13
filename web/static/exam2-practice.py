def splaz(n: int) -> int:
    count = 0
    while count < 100 and n != 1:
        if n % 3 == 0:
            n //= 3
        else:
            n = 2*n + 1
        count += 1
    if count < 100:
        return count
    else:
        return -1

def input_integer(prompt: str) -> int:
    valid = False
    while not valid:
      value1 = input(prompt)
      if value1.isdigit() or value1[0] == '-' and value1[1:].isdigit():
        valid = True
        value1 = int(value1)
      else:
        print("Not a number, try again!")
    return value1


def get_sum():
    value1 = input_integer("Enter a number:")

    value2 = input_integer("Enter another number:")

    return value1 + value2
