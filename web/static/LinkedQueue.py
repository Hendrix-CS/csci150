from Link import *

class LinkedQueue:

    # Methods:

    def __init__(self):
        self.front = None
        self.back  = None
        self.num_items = 0

    # Add a new item to the "back".
    def enqueue(self, item):

        new_link = Link(item)
        if self.back is None:
            self.back = self.front = new_link
        else:
            self.back.setNext(new_link)
            self.back = new_link

        self.num_items += 1

        # Wrong way!
        # new_link = Link(item)
        # new_link.setNext(self.back)
        # self.back = new_link
        # if self.front is None:
        #     self.front = new_link
        #
        # self.num_items += 1

    # Remove an item from the "front" and return it.
    def dequeue(self):
        link_to_remove = self.front
        self.front = self.front.getNext()

        self.num_items -= 1
        if self.num_items == 0:
            self.back = None

        return link_to_remove.getItem()

    # Return the number of items in the queue
    def length(self):
        return self.num_items

    # Return whether or not the queue is empty
    def is_empty(self):
        return self.length() == 0

    def __repr__(self):
        return ""
