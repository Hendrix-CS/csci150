from typing import *

def read_file_data(filename: str) -> Tuple[List[str], List[int], List[int]]:
    names = []
    prices = []
    quantities = []
    with open(filename, 'r') as file_in:
        for line in file_in:
            line = line.strip()
            line_parts = line.split(',')
            names.append(line_parts[0])
            prices.append(int(line_parts[1]))
            quantities.append(int(line_parts[2]))
    return names, prices, quantities


def main():
    filename = input("Enter filename of log: ")
    names, prices, quantities = read_file_data(filename)
    done = False
    while not done:
        request = input("Enter 'income', 'items', 'popular', or 'quit': ")
        if request == 'quit':
            done = True
        elif request == 'income':
            total = 0
            for i in range(len(prices)):
                total += prices[i] * quantities[i]
            print(f"Total income: ${total // 100}.{total % 100}")
        elif request == 'items':
            total = 0
            for q in quantities:
                total += q
            print(f"Total items sold: {total}")


main()
