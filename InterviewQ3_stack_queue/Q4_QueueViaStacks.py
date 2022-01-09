# Q4_QueueViaStacks
"""
Implement Queue class which implements a queue using two stacks
"""

class Stack:
    def __init__(self):
        self.list = [] 

    def __len__(self):
        return len(self.list)

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None 
        return self.list.pop()

class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        if len(self.inStack) == 0:
            return "The queue is empty"
        item = self.inStack.pop()
        while item:
            self.outStack.push(item)
            item = self.inStack.pop()
        
        value = self.outStack.pop()
        item = self.outStack.pop()
        while item:
            self.inStack.push(item)
            item = self.outStack.pop()

        return value 

q = QueueViaStack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())