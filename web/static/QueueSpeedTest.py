from ListQueue import *
from LinkedQueue import *

import time

def main():
    q = LinkedQueue()

    for power in range(1,20):

        n = 2 ** power

        start = time.time()

        for i in range(n):
            q.enqueue(i)
        while (not q.is_empty()):
            q.dequeue()

        end = time.time()

        print(str(power) + " " + str(end - start))

main()