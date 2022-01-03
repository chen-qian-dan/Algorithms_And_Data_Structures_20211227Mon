# Circular Singly Linked List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class CircularSinglyLinkedList:
    def __init__(self):
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
        node.next = node
        self.head = node
        self.tail = node 
       
        return "The list has been created"



csll: CircularSinglyLinkedList = CircularSinglyLinkedList()
csll.create(1)

print([node.value for node in csll])