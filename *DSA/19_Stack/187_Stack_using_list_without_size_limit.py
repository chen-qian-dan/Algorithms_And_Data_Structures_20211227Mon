
"""
Stack using list without size limit

1. create 
2. push
3. pop
4. peak
5. isEmpty
6. isFull
7. deleteStack
"""

class Stack:
    def __init__(self):
        """
        first in, last out
        push at the end
        pop at the end
        """
        self.list = list()

    def __str__(self):
        return " -> ".join(str(v) for v in self.list)

    def push(self, val):
        self.list.append(val)

    def pop(self):
        if len(self.list) == 0:
            raise ValueError("The stack is empty")
        return self.list.pop()

    def peek(self):
        if len(self.list) == 0:
            raise ValueError("The stack is empty")
        return self.list[-1]

    def isEmpty(self):
        return True if len(self.list) == 0 else False 
    
    def deleteStack(self):
        self.list.clear()
        



stack = Stack()
stack.push(1)
stack.push(2)
print(stack)
# print(stack.pop())
# print(stack)
# print(stack.peek())
# print(stack)
stack.deleteStack()
print(stack)


