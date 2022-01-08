# queue_usingLinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next 

    def __str__(self):
        values = [str(node.value) for node in self]
        return ' '.join(values)

    

