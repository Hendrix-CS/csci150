# Integer input validation
def int_input(prompt: str) -> int:
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
    t1 = int_input("Type an integer. ")
    t2 = int_input("Type the second integer. ")
    t3 = int_input("Type the third integer. ")
    t4 = int_input("Type the fourth integer. ")
    t5 = int_input("Type the fifth integer. ")

    print(f"You typed {t1}, {t2}, {t3}, {t4}, then {t5}.")

    average = (t1 + t2 + t3 + t4 + t5) / 5

    # https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python
    print(f"Their average is {average:.2f}.")

def main2():

    num = int_input("How many numbers do you want to average? ")
    t = []
    count = 0
    while count < num:
        t.append(int_input("Type an integer. "))
        count += 1

    print(f"You typed {t}.")

    sum_num = 0
    i = 0
    while i < count:
        sum_num += t[i]
        i += 1

    average = sum_num / count

    # https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python
    print(f"Their average is {average:.2f}.")

