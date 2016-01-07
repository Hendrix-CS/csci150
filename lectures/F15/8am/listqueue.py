# CSCI 150
# 30 November 2015
# Queues

# Queue:
#   - a sequence/list of things
#   - can add to only one end
#   - can remove only from the other end
#
# Can model things like:
#   - Line at a bank or grocery store
#   - People or programs waiting to print something
#     or use some other resource (e.g. network)

# Let's make a Queue class
# What methods should it have?
#   - add(item)
#   - remove()
#   - is_empty()
#   - size()

# This superclass defines the interface for a
#   queue.  We will make two subclasses, with
#   two different ways of implementing the
#   methods.
class Queue:
    # Add an item to the back
    def add(item):
        pass

    # Remove an item from the front and return it
    def remove():
        pass

    def is_empty():
        pass

    def size():
        pass


# Implementation #1: using a list

class ListQueue(Queue):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return "Front | " + str(self.queue)

    def is_empty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    def remove(self):
        return self.queue.pop(0)

    def add(self, item):
        self.queue.append(item)

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
