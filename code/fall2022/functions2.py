import math

def quadratic(a: float, b: float, c: float) -> float:
    disc: float = b ** 2 - 4*a*c
    return (-b + math.sqrt(disc))/(2*a)

def main():
    x: float = 5
    y: float = quadratic(x, x+1, x-12)
    print(y)

main()