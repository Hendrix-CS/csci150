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

##########################


class Node:
    # Variables:
    #   - value  (any type)
    #   - next    (Node)
    def __init__(self, value):
        self.value = value
        self.next   = None

    # We'll refer to node.next and node.value
    # directly instead of making getter and setter methods

class LinkedQueue(Queue):
    # Variables:
    #    - front (Node)
    #    - back (Node)

    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front == None

    # Can make this faster by storing current size
    # in self.size (update it when adding & removing)
    # then just return it here.
    def size(self):
        count = 0
        cur = self.front
        while cur != None:
            count += 1
            cur = cur.next

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def remove(self):
        if self.is_empty():
            return None
        else:
            to_return = self.front.value
            self.front = self.front.next
            if self.front == None:
                self.back = None
            return to_return

import time

def test():
    q = LinkedQueue()

    for i in range(10):
        q.add(i)
    for i in range(10):
        print q.remove()
        

def main():
    q = LinkedQueue()

    for power in range(0,7):
        
        start = time.time()
        for i in range(10**power):
            q.add(i)
        for i in range(10**power):
            q.remove()
        end = time.time()

        print power, (end - start)


    
