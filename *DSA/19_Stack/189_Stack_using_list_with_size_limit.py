"""
Stack using list with size limit

1. create 
2. push
3. pop
4. peak
5. isEmpty
6. isFull
7. deleteStack
"""

class Stack:
    def __init__(self, capacity: int):
        self.list = list()
        self.capacity = capacity 

    def __str__(self):
        return " -> ".join([str(v) for v in self.list])

    def isFull(self):
        return True if len(self.list) >= self.capacity else False 

    def isEmpty(self):
        return True if len(self.list) == 0 else False 

    def push(self, val):
        if self.isFull():
            print("The stack is full")
        else:
            self.list.append(val)
        
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]

    def deleteStack(self):
        self.list = list()
        self.capacity = None 

        
stack = Stack(5)
print(stack)
stack.push(1)
stack.push(2)
print(stack)
# print(stack.pop())
# print(stack)
# print(stack.peek())
# print(stack)
stack.deleteStack()
print(stack)

