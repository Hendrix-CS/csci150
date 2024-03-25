filename = input("Enter filename: ")
with open(filename) as f:
    lines = f.readlines()
    lines.sort()
    print(lines)