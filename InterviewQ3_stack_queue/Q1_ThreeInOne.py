"""
Describe how you could use a single Python list to implement three stacks. 

1. Problem:
Suppose no size limit for stack: Stack has size limit, list has size limit too
2. Input:
"""

class MultiStack:
    def __init__(self, stacksize: int):
        self.stackCount = 3
        self.list = [None] * stacksize * self.stackCount

        self.sizes = [0] * self.stackCount
        self.stacksize = stacksize

    
    def isFull(self, stackIndex):
        return True if self.sizes[stackIndex] == self.stacksize else False 

    def isEmpty(self, stackIndex):
        return True if self.sizes[stackIndex] == 0 else False 

    def indexOfTop(self, stackIndex):
        offset = self.stacksize * stackIndex
        return offset - 1 + self.sizes[stackIndex]

    def push(self, stackIndex, value):
        if self.isFull(stackIndex):
            return "The stack is full"
        else:
            self.sizes[stackIndex] += 1
            self.list[self.indexOfTop(stackIndex)] = value 

    def pop(self, stackIndex):
        if self.isEmpty(stackindex):
            return "The stack is empty"
        else:
            value = self.list[self.indexOfTop(stackIndex)]
            self.sizes[stackIndex] -= 1
            return value 

    def peek(self, stackIndex):
        if self.isEmpty(stackindex):
            return "The stack is empty"
        else:
            value = self.list[self.indexOfTop(stackIndex)]
            return value  


ms = MultiStack(3)
ms.push(2, 1)
print(ms.list)