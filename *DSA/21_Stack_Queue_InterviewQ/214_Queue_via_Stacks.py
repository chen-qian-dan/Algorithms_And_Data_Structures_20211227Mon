"""
Implement Queue class which implements a queue using two stacks
"""

from collections import deque 

class Stack:
    def __init__(self):
        self.q = deque()

    def __str__(self):
        ret = list()
        for i in range(len(self.q)):
            ret.append(self.q[i])
        return  "->".join(str(v) for v in ret) 

    def isEmpty(self):
        return True if len(self.q) == 0 else False 

    def push(self, val):
        self.q.appendleft(val)

    def pop(self):
        if self.isEmpty():
            raise ValueError("The stack is empty")
        return self.q.popleft()

    def peek(self):
        if self.isEmpty():
            raise ValueError("The stack is empty")
        return self.q[0]

    def deleteStack(self):
        self.q.clear()


class Queue:
    def __init__(self):
        self.primeStack = Stack()
        self.secondStack = Stack() 

    def isEmpty(self):
        return True if self.primeStack.isEmpty() else False 

    def enqueue(self, val):
        self.primeStack.push(val)

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            while not self.primeStack.isEmpty():
                val = self.primeStack.pop()
                self.secondStack.push(val)
            ret = self.secondStack.pop()

            while not self.secondStack.isEmpty():
                val = self.secondStack.pop()
                self.primeStack.push(val)

            return ret 

    def deleteQueue(self):
        self.primeStack = Stack()
        self.secondStack = Stack()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
