filename = input("Enter filename: ")
with open(filename) as f:
    contents = f.read()
    blocks = contents.split("\n\n")
    for i in range(len(blocks)):
        print(f"Block {i + 1}:")
        print(blocks[i])
        print()