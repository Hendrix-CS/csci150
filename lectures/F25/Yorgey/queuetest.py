from fastqueue1 import *
from datetime import *

def main():

    for k in range(1, 20):
        t = datetime.now()

        print("Queueing...")
        q = Queue()
        for i in range(2 ** k):
            q.enqueue(i)
        print("Done enqueueing!")
        j = 0
        while not q.is_empty():
            if j != q.dequeue():
                print("Wrong!!!")
            j += 1
        print("Done dequeueing!")

        # print("Done!!")

        print(f"2^{k}: {(datetime.now() - t).total_seconds()}")

main()