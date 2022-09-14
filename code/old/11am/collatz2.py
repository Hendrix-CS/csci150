# given an integer n
# if n is even
#     divide it by 2
# otherwise it is odd
#     multiply by 3 and add 1
# repeat the process until n is 1

########
# This function brings in a number
# and determines the next in the sequence
def next_number(oogie: int) -> int:
    if oogie % 2 == 0:
        return oogie // 2
    else:
        return oogie * 3 + 1

#######
# calculates the collatz sequence for a given number
def collatz(n: int) -> int:
    c = 0
    while n != 1:
        n = next_number(n)
        c += 1
    return c

#######
# Runs the main program
def main():
    max = int(input("What is the max number do you want to test? "))
    n = 1
    while n <= max:
        c = collatz(n)
        print(f"{n}, {c}")
        n += 1

main()
