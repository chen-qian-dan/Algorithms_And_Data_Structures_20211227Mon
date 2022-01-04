# Doubly Linked List

# create -----------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value 
        self.pre = None 
        self.next = None 
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 


    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next

    def append(self, value):
        node: Node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            node.prev = self.tail 
            self.tail.next = node 
            self.tail = node 




dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)
dll.append(2)
print([node.value for node in dll])