"""
Q2: Stack Min
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1). 

if push, pop and min are in O(1), then need to use linked list to make this stack 
"""
import math 

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Stack:
    def __init__(self):
        # push and pop at the head
        self.head = None 
        self.minHead = None 
        self.minValue = math.inf

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 

    def __str__(self):
        values = [node.value for node in self]
        values = [str(v) for v in values]
        return ' '.join(values)

    def push(self, value):
        self.minValue = min(self.minValue, value)
        node = Node(self.minValue)
        if not self.minHead:
            self.minHead = node 
        else:
            node.next = self.minHead
            self.minHead = node 

        node = Node(value)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node 

    def pop(self):
        if not self.head:
            return "The stack is empty"
        else:
            value = self.head.value 
            self.head = self.head.next 

            self.minHead = self.minHead.next 
            return value 

    def min(self):
        if not self.minHead:
            return "The stack is empty"
        else:
            return self.minHead.value 




s = Stack()
s.push(9)
print(s)
print(s.min())
s.push(10)
print(s.min())

s.push(8)
print(s.min())
print(s)
s.pop()
print(s.min())



