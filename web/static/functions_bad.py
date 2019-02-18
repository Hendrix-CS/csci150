
# WRONG way to use functions: each calls the next thing that should happen.

# def f1():
#     print("1. Do some stuff")
#     f2()
#
# def f2():
#     print("2. Do some other stuff")
#     f3()
#
# def f3():
#     print("3. Do the stuff")
#
# f1()

# Right way:

def main():
    f1()
    f2()
    f3()

def f1():
    print("1. Do some stuff")
    # f1 doesn't know or care what comes next.

def f2():
    print("2. Do some other stuff")

def f3():
    print("3. Do the stuff")

