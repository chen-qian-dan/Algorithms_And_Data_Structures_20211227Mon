

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
    



stack = Stack()
stack.push(1)
stack.push(2)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack)
stack.deleteStack()
print(stack)