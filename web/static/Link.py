class Link:
    # Variables:
    # - item  (any type)
    # - next  (reference to another Link)

    def __init__(self, item):
        self.item = item
        self.next = None   # Not referencing anything initially.

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, new_item):
        self.item = new_item

    def setNext(self, new_next):
        self.next = new_next
