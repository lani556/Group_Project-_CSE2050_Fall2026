from node import Node

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.counter = 0


    def add_first(self, item):
        if self._tail is None:
            self._tail = self._head
    
        self._head = Node(item, self._head)
        
        self.counter += 1


    def add_last(self,item):
        node = Node(item)
        if self._head is None:
            self._head = node  
            self.counter += 1 
        elif self.counter == 1:
            self._tail = node
            self._head.next = self._tail
            self.counter += 1 
        else:
            self._tail.next = node
            self.counter += 1 
        
        

    def remove_first(self):
        if self._head is None:
            return None 
        prev_first = self._head.data
        self._head = self._head.next
        self.counter -= 1
        return prev_first
        

    def get_first(self):
        return self._head.data

    def is_empty(self):
        return True if self._head is None and self._tail is None else False

    def size(self):
        return self.counter
