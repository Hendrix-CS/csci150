def g(z: int):
    z = z*3
    print(z)

def f(x: int):
    g(x)
    g(x + 2)
    print(x)

f(3)
