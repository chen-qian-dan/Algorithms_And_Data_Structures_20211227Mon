
from random import randint 

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.prev = None 
        self.next = None 

    def __str__(self): # when print(node), will call this function
        return str(self.value)


class LinkedList:
    """
    Singly linked list
    """
    def __init__(self, values = None):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node 
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        count: int = 0
        node: Node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def add(self, value):
        node: Node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 
        return self.tail
        
    def generate(self, n, minValue, maxValue):
        self.head = None
        self.tail = None 
        for i in range(n):
            self.add(randint(minValue, maxValue))


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)


    
