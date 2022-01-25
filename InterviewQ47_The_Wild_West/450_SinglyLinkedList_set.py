"""
450 - Singly Linked List - Set
The func accept an index and a value and update the value of the node in the SinglyLinkedList at the index with new value. 
It should return True if the node is updated successfully or False if an invalid index is passed in. 

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(1)
singlyLinkedList.push(2)    

singlyLinkedList.set(0, 10) # True
singlyLinkedList.set(1, 20) # True
singlyLinkedList.length # 2
singlyLinkedList.head.val # 10

singlyLinkedList.set(10, 10) # False
singlyLinkedList.set(2, 100) # False

singlyLinkedList.head.next.val # 20


# Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def set(self, index, value):
        # TODO
"""

# Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def set(self, index, value):
        # TODO
        if self.length == 0:
            return False 
        if index < 0 or index >= self.length:
            return False 

        node = self.head 
        for i in range(index):
            node = node.next 
        node.val = value 
        return True 
            