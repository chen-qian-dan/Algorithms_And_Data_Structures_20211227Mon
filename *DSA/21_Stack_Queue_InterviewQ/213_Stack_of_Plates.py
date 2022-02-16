"""
Q3: Stack of Plates
Imagine a (literal) stack of plates. 
If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity, 
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, 
pop() shoud return the same value as it would if there were just a single stack).

Follow up:
Implement a function popAt(int index) which performs a pop operation on a specific sub - stack. 

if not time complexity limitation, can use 2-D list
"""
from collections import deque 

class StackPlate:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.stacks = deque()

    def __str__(self):
        ret = list()
        for s in self.stacks:
            for v in s:
                ret.append(str(v))
        return " -> ".join(ret)

    def push(self, val):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            newQ = deque()
            newQ.appendleft(val)
            self.stacks.append(newQ)
        else:
            self.stacks[-1].appendleft(val)

    def pop(self):
        if len(self.stacks) == 0:
            return "The set of stacks is empty"
        else:
            val = self.stacks[-1].popleft()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            return val 


stackPlate = StackPlate(3)
print(stackPlate)
stackPlate.push(1)
stackPlate.push(2)
stackPlate.push(3)
stackPlate.push(4)
stackPlate.push(5)
print(stackPlate)

print(stackPlate.pop())
print(stackPlate)
print(stackPlate.pop())
print(stackPlate)
print(stackPlate.pop())
print(stackPlate)
