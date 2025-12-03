# Queue = sequence of items where we can put items in one end and take them out from the other end.
#   e.g. line of people waiting at the grocery store checkout
#   e.g. list of requests received by a web server

class Queue:

    def __init__(self):
        self.items = []

    # Add a new item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove an item from the "front" of the queue and return it.
    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return len(self.items) == 0
