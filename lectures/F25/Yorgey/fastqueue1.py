class Queue:

    def __init__(self):
        self.items = []
        self.front = 0

    # Add a new item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove an item from the "front" of the queue and return it.
    def dequeue(self):
        item = self.items[self.front]
        self.front += 1
        return item

    def is_empty(self) -> bool:
        return self.front == len(self.items)
