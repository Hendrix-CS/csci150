def squid(x: int) -> int:
    zebra = x + 2
    x *= 2
    print(x)
    return zebra

def elephant(horse: str) -> int:
    x = len(horse)
    z = squid(x) + squid(x-1)
    return z

def main():
    print(elephant('lion'))
    print("Done!")

main()
