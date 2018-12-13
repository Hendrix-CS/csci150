from ListQueue import *

def main():
    q = ListQueue()

    for i in range(10):
        q.enqueue(i)

    print(q)
    print(q.length())

    while (not q.is_empty()):
        print(q.dequeue())

    print(q)
    print(q.length())

main()