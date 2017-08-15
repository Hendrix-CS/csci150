# Queues

import time

class ListQueue:
    # Variables:
    #    - elements (list of whatever you want)

    # Methods:
    #    - __init__(): makes a new empty queue
    #    - enqueue(item): add an item to the back
    #    - dequeue(): remove and return an item from the front
    #    - size(): return # of items in the queue

    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)

def main():
    for k in range(1,20):
        pow10 = 2 ** k

        start_time = time.time()

        # print("Enqueueing with pow10 = " + str(pow10))
        q = LinkedQueue()
        for n in range(pow10):
            q.enqueue(n)
        # print("Dequeueing with pow10 = " + str(pow10))
        for n in range(pow10):
            q.dequeue()

        end_time = time.time()

        print (str(pow10) + " " + str(end_time - start_time))


# Linked list

# A linked list is made of nodes.
# Each node has a value and a reference to another node
#    (or None if there isn't another node).

class Node:
    # Variables:
    #    - value (any type)
    #    - next (Node)

    # Create a node with the given value, which is not
    # pointing to another node yet.
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, new_next):
        self.next = new_next

class LinkedQueue:

    def __init__(self):
        self.front = None
        self.back = None

    def size(self):
        count = 0
        cur_node = self.front
        while (cur_node != None):
            count += 1
            cur_node = cur_node.get_next()

        return count

    def enqueue(self, item):
        new_node = Node(item)
        if (self.back == None):
            self.back = new_node
            self.front = new_node
        else:
            self.back.set_next(new_node)
            self.back = new_node

    def dequeue(self):
        to_return = self.front.get_value()
        self.front = self.front.get_next()

        if (self.front == None):
            self.back = None

        return to_return


    
