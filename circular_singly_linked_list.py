# Circular Singly Linked List


class Node:
    def __init(self, value):
        self.value = value
        self.next = None 

class CircularSinglyLinkedList:
    def __init__(self, value):
        self.head = None 
        self.tail = None 


    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            if node == self.tail:
                break 
            node = node.next
