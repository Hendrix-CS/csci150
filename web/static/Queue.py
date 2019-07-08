class Queue:

    # Variables:
    #   - elems (list)

    def __init__(self):
        self.elems = []

    def size(self) -> int:
        return len(self.elems)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def enqueue(self, item):
        self.elems.append(item)

    def dequeue(self):
        return self.elems.pop(0)


def main():
    q = Queue()
    for i in range(1000000):
        q.enqueue(i)

    sum: int = 0
    while not q.isEmpty():
        sum += q.dequeue()

    print(sum)

main()