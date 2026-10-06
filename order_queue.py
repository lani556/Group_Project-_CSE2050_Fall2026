class OrderQueue():
    def __init__(self):
        """Initializes an empty order queue"""
        self.queue = [] #This should be linkedlist

    def enqueue(self, item):
        """Adds an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the item from the front of the queue. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        """Returns the item at the front of the queue without removing it. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def size(self):
        """Returns the number of items in the queue"""
        return len(self.queue)

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise"""
        return len(self.queue) == 0



# test1 = OrderQueue()
# test1.enqueue("Order 1")
# print(test1.dequeue())