"""
Q2: Stack Min
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1). 

if push, pop and min are in O(1), then need to use linked list to make this stack 
"""

class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None 

class Linked_List:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __str__(self):
        ret = list()
        cur = self.head 
        while cur:
            ret.append(str(cur.val))
            cur = cur.next 
        return " -> ".join(ret)

    def enqueue(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode 
        else:
            newNode.next = self.head 
            self.head = newNode

            
    def dequeue(self):
        if self.head is None:
            return "The queue is empty"
        elif self.head == self.tail:
            val = self.head.val 
            self.head = None 
            self.tail = None 
            return val 
        else:
            val = self.head.val 
            self.head = self.head.next 
            return val 


class Stack:
    def __init__(self):
        self.items = Linked_List()
        self.minimum = Linked_List()

    def __str__(self):
        return str(self.items)

    def push(self, val):
        self.items.enqueue(val)
        if self.items.head == self.items.tail:
            self.minimum.enqueue(val)
        else:
            self.minimum.enqueue(min(val, self.minimum.tail.val))

    def pop(self):
        val = self.items.dequeue()
        minima = self.minimum.dequeue()
        return val 

    def getMin(self):
        return self.minimum.head.val



s = Stack()
s.push(9)
print(s)
print(s.getMin())
s.push(10)
print(s.getMin())

s.push(8)
print(s.getMin())
print(s)
s.pop()
print(s.getMin())

            

