"""
Describe how you could use a single Python list to implement three stacks. 

1. Problem:
Suppose no size limit for stack: Stack has size limit, list has size limit too
2. Input:
"""
from inspect import stack


class MultiStack:
    def __init__(self, stacksize: int):
        self.items = [None] * stacksize * 3
        self.sizes = [0] * stacksize
        self.maxSize = stacksize

    
    def isFull(self, stackIndex):
        return True if self.sizes[stackIndex] >= self.maxSize else False 
        

    def isEmpty(self, stackIndex):
        return True if self.sizes[stackIndex] == 0 else False 
        
    def indexOfTop(self, stackIndex):
        offset = self.maxSize * stackIndex
        return offset + self.sizes[stackIndex] - 1
        

    def push(self, stackIndex, val):
        if self.isFull(stackIndex):
            print("The stack is full")
        else:
            self.items[self.indexOfTop(stackIndex)] = val 
            self.sizes[stackIndex] += 1
        
    def pop(self, stackIndex):
        if self.isEmpty(stackIndex):
            print("The stack is empty")
        else:
            val = self.items[self.indexOfTop[stackIndex]]
            self.sizes[stackIndex] -= 1
            return val 
        

    def peek(self, stackIndex):
        if self.isEmpty(stackIndex):
            print("The stack is empty")
        else:
            val = self.items[self.indexOfTop[stackIndex]]
            return val 
        


ms = MultiStack(3)
ms.push(2, 1)
print(ms.items)