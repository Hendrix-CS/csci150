from typing import *


class SalesInfo:
    def __init__(self, file_line: str):
        file_line = file_line.strip()
        line_parts = file_line.split(',')
        self.name = line_parts[0]
        self.price = int(line_parts[1])
        self.quantity = int(line_parts[2])

    def revenue(self) -> int:
        return self.price * self.quantity


def read_file_data(filename: str) -> List[SalesInfo]:
    result = []
    with open(filename, 'r') as file_in:
        for line in file_in:
            result.append(SalesInfo(line))
    return result


def main():
    filename = input("Enter filename of log: ")
    file_data = read_file_data(filename)
    done = False
    while not done:
        request = input("Enter 'income', 'items', 'popular', or 'quit': ")
        if request == 'quit':
            done = True
        elif request == 'income':
            total = 0
            for data in file_data:
                total += data.revenue()
            print(f"Total income: ${total // 100}.{total % 100}")
        elif request == 'items':
            total = 0
            for data in file_data:
                total += data.quantity
            print(f"Total items sold: {total}")
        elif request == 'popular':
            most_popular = 0
            for i in range(1, len(file_data)):
                if file_data[i].quantity > file_data[most_popular].quantity:
                    most_popular = i
            print(f"Most popular item: Sold {file_data[most_popular].quantity} of {file_data[most_popular].name}.")


main()
