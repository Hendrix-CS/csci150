
def double(x: int) -> int:
    x = 2 * x
    return x + 1

def main():
    x = double(3)
    print(x)
    x = double(double(x))
    print(x)

main()