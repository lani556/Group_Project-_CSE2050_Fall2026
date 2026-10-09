#from linkedlist import LinkedList

class Stack:
    def __init__(self):
        """Initializes an empty stack"""
        self.items = [] #This needs to be linked list i think -> LinkedList()

    def push(self, item):
        """Adds an item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top of the stack. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        """Returns the item at the top of the stack without removing it. Returns None if empty"""
        if self.is_empty():
            return None
        else:
            return self.items[-1]
    
    def is_empty(self):
        """Returns True if the stack is empty, False otherwise"""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the stack"""
        return len(self.items)

    
