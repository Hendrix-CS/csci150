# given an integer n
# if n is even
#     divide it by 2
# otherwise it is odd
#     multiply by 3 and add 1
# repeat the process until n is 1
def collatz(n:int):
    c = 0
    while n != 1:
        print(f"{c}:{n}")
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        c += 1
    print(f"this ran {c} times.")

def main():
    n = int(input("What number do you want to test? "))
    collatz(n)

main()
