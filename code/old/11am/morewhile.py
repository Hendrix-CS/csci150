# Write the "explode" function, that brings in
# a string parameter, and prints it off
# one character at a time, for example
# with the argument "cat"
# it would print
# c
# a
# t
def explode(word: str):
    car = 0
    while car < len(word):
        print(word[car])
        car += 1

# Integer input validation
def int_input(prompt: str) -> int:
#    x = input(prompt)
#    while not x.isdigit() and int(x) > max:
#        print("That's not an integer.")
#        x = input(prompt)
#   return int(x)

    valid = False
    while not valid:
        x = input(prompt)
        if x.isdigit():
            valid = True
        elif (x[0] == "-" or x[0] == "+") and x[1:].isdigit():
            valid = True
        else:
            print("That's not an integer.")
    return int(x)



def main():
    #w = input("What word do you want to explode? ")
    #explode(w)
    t = int_input("Type an integer. ")
    print(f"{t + 2} is 2 more than you typed.")

main()
