def q():
    r = 5 / 0
    print("Yay!")

def g(z: int):
    z = z*3
    q()
    print(z)

def f(x: int):
    g(x)
    g(x+2)
    print(x)

f(3)
