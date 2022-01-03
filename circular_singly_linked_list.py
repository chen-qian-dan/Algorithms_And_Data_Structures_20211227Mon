# Circular Singly Linked List

from typing import Counter, Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.count: int = 0


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
        self.count += 1
       
        return "The list has been created"

    
    def insert(self, value, location):
        nodeNew: Node = Node(value)
        self.count += 1
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



    def deleteANode(self, location: int):
        if location < -1 or location > self.count - 1:
            print("location is out of range[0, {self.count}]")
            return 
        self.count -= 1
        # delete the first node
        if location == 0:
            if self.head == self.tail:
                self.head = None 
                self.tail = None 

            else:
                self.head = self.head.next
                self.tail.next = self.head 

        # delete the last node
        elif location == -1 or location == self.count - 1:
            if self.head == self.tail:
                self.head = None 
                self.tail = None  
            else:
                node: Node = self.head
                while node.next != self.tail:
                    node = node.next
                self.tail = node
                self.tail.next = self.head 
        # delete the middle node 
        else:
            index = 0
            node: Node = self.head
            while index < location - 1:
                index += 1
                node = node.next
                
            node.next = node.next.next


    def deleteEntireList(self):
        self.count = 0
        self.head = None 
        self.tail.next = None 
        self.tail = None 


csll: CircularSinglyLinkedList = CircularSinglyLinkedList()
csll.insert('a', 0)
csll.insert('b', -1)
csll.insert('c', 0)
csll.insert('d', 1)
csll.insert('d', 3)
csll.insert('e', 5)
print([node.value for node in csll])
# csll.traverse()
# print(csll.search(1))
# csll.deleteANode(6)
csll.deleteEntireList()
print([node.value for node in csll])