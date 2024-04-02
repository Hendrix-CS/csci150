from typing import *


def read_file_data(filename: str) -> List[Dict]:
    result = []
    with open(filename, 'r') as file_in:
        for line in file_in:
            line = line.strip()
            line_parts = line.split(',')
            data = {}
            data['name'] = line_parts[0]
            data['price'] = int(line_parts[1])
            data['quantity'] = int(line_parts[2])
            result.append(data)
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
                total += data['price'] * data['quantity']
            print(f"Total income: ${total // 100}.{total % 100}")
        elif request == 'items':
            total = 0
            for data in file_data:
                total += data['quantity']
            print(f"Total items sold: {total}")
        elif request == 'popular':
            most_popular = 0
            for i in range(1, len(file_data)):
                if file_data[i]['quantity'] > file_data[most_popular]['quantity']:
                    most_popular = i
            print(f"Most popular item: Sold {file_data[most_popular]['quantity']} of {file_data[most_popular]['name']}.")


main()
