
# "Explode" a string by printing each character on its own line.
# e.g. explode("hey") will print
# h
# e
# y
def explode(s: str):
    i: int = 0
    while i < len(s):
        print(s[i])
        # i += 1

    # conceptually we want to do this:
    # print(s[0])
    # print(s[1])
    # print(s[2])
