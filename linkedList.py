class Node:

    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class linkedList:
    def __init__():
        self._head = None
        self._tail = None
        self.counter = 0


    def add_first(item):
        if self._tail is None:
            self._tail = self._head
        self._head = Node(item, self._head)
        self.counter += 1


    def add_last(item):
        if self._head is None:
            addfirst(item)
        else:
            currentnode = self._head
            self._tail.next = Node(item)
            self._tail = self._tail.next
            self.counter += 1

    def remove_first():
        if self._head is None:
            return None 
        remove = self._head.data
        self._head = Node(self._head.next,self._head.next.next)
        return remove
        

    def get_first():
        return self._head.data

    def is_empty(self):
        return True if self._head is None and self._tail is None

    def size(self):
        return self.counter
