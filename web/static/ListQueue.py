# Queues!

class ListQueue:

    # Methods:

    def __init__(self):
        self.items = []
        self.num_items = 0

    # Add a new item to the "back".
    def enqueue(self, item):
        self.items.append(item)
        self.num_items += 1

    # Remove an item from the "front" and return it.
    def dequeue(self):
        self.num_items -= 1
        return self.items.pop(0)

    # Return the number of items in the queue
    def length(self):
        return self.num_items

    # Return whether or not the queue is empty
    def is_empty(self):
        return self.length() == 0

    def __repr__(self):
        return "Front: " + str(self.items) + " : Back"
