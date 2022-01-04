# Circular Doubly Linked List


# create -------------------------------------
class Node:
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 

class CircularDoublyLinkedList:

    def __init__(self):
        self.count: int = -1
        self.head = None 
        self.tail = None 
        

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            if node == self.tail:
                break 
            node = node.next 

    def create(self, value):
        node: Node = Node(value)
        self.head = node 
        self.tail = node
        node.next = node 
        node.prev = node 
        print("Create successfully")


# create -------------------------------------
cdll: CircularDoublyLinkedList = CircularDoublyLinkedList()
cdll.create(1)
print([node.value for node in cdll])


 