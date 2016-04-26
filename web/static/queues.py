# Queues
# "First-in, first-out" data structure
# Can put  things in one end ("back") and take things off of
# the other end ("front")
# Can model things like:
#   - line in a grocery store
#   - line in a bank
#   - data being sent over a network
#   - processes waiting to use the processor

# Operations:
#   - size
#   - is_empty
#   - add
#   - remove

# Generic class for queues
class Queue:
    # Number of items in the queue
    def size(self):
        pass

    # Is the queue empty?
    def is_empty(self):
        pass

    # Add a new item to the back
    def add(self, item):
        pass

    # Remove item from the front and return it, or None if the queue was empty
    def remove(self):
        pass

# We're going to make two different implementations of Queue.

# First implementation: use a list.

class ListQueue(Queue):
    # Variable:
    #   elements (list): end of the list is the back of the queue

    def __init__(self):
        self.elements = []

    def __repr__(self):
        return "Front | " + str(self.elements)

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def add(self, item):
        self.elements.append(item)

    def remove(self):
        return self.elements.pop(0)

import time

def main():
    q = ListQueue()

    for power in range(0,7):
        
        start = time.time()
        for i in range(10**power):
            q.add(i)
        for i in range(10**power):
            q.remove()
        end = time.time()

        print power, (end - start)


    
