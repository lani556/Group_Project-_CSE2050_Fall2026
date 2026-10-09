from linkedList import LinkedList
from stack import Stack

class OrderQueue():
    def __init__(self):
        """Initializes an empty order queue"""
        self.queue = LinkedList()

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.add_last(item)

    def dequeue(self):
        """Removes and returns the item from the front of the queue. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.queue.remove_first()

    def peek(self):
        """Returns the item at the front of the queue without removing it. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.queue.peek()

    def size(self):
        """Returns the number of items in the queue"""
        return self.queue.size()

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return self.queue.is_empty()



# test1 = OrderQueue()
# test1.enqueue("Order 1")
# print(test1.dequeue())