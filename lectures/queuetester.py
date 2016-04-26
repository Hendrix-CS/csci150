import queues
import time

def main():
    q = ListQueue()

    for power in range(1,7):

        # Get starting time
        start = time.time()
        # Compute 10^power
        n = 10 ** power

        # Add and remove 10^power times
        for i in range(n):
            q.add(i)
        for i in range(n):
            q.remove()

        # Get ending time
        end = time.time()

        # Print power and elapsed time in seconds
        print power, end - start

main()
