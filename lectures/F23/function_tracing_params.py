
def g(s: int) -> int:
    z = 3
    return s + z

def main():
    z = g(7)
    print("In main")
    z = z + g(z)
    print(z)

main()