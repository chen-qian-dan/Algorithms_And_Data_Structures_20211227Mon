# Circular Singly Linked List

from typing import Optional

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

    
    def insert(self, value, location):
        nodeNew: Node = Node(value)
        # if the list is empty
        if self.head is None:
            nodeNew.next = nodeNew 
            self.head = nodeNew
            self.tail = nodeNew
            return True 

        # insert at the beginning 
        if location == 0:
            nodeNew.next = self.head
            self.head = nodeNew
            self.tail.next = nodeNew

        # insert at the end
        elif location == -1:
            self.tail.next = nodeNew
            self.tail = nodeNew
            self.tail.next = self.head

        # insert at the middle 
        else:
            node: Node = self.head
            index: int = 0
            if location == 5:
                print("True")
            while index < location - 1 and node != self.tail:
                index += 1
                node = node.next

            if node == self.tail:
                self.tail.next = nodeNew
                self.tail = nodeNew
                self.tail.next = self.head
            else:
                nodeNew.next = node.next
                node.next = nodeNew



    def traverse(self):
        node: Optional[Node, None] = self.head
        while node:
            print(node.value)
            if node == self.tail:
                break 
            else:
                node = node.next


    def search(self, value):
        index: int = -1
        node: Node = self.head
        while node:
            index += 1
            if node.value == value:
                return index
            if node == self.tail:
                break 
            node = node.next
        return -1 


csll: CircularSinglyLinkedList = CircularSinglyLinkedList()
csll.insert('a', 0)
csll.insert('b', -1)
csll.insert('c', 0)
csll.insert('d', 1)
csll.insert('d', 3)
csll.insert('e', 5)
print([node.value for node in csll])
# csll.traverse()
print(csll.search(1))