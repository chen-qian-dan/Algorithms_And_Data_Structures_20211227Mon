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

if not time complexity limitation, can use 2-D list"""
from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value 
        self.next: Optional[Node] = None 

class Stack:
    # push and pop at the head 
    def __init__(self, maxSize: int):
        self.maxSize: int = maxSize 
        self.head: Optional[Node] = None
        self.size: int = 0 

    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next 

    def __str__(self):
        values = [node.value.value for node in self]
        values = [str(v) for v in values]
        return ' '.join(values)

    def isFull(self):
        return True if self.size == self.maxSize else False 

    def isEmpty(self):
        return True if self.size == 0 else False 


    def push(self, value: int ):
        if self.size == self.maxSize:
            print("The Stack is full")
        else:
            node = Node(value)
            node.next = self.head 
            self.head = node 
            self.size += 1
        
    def pop(self):
        if self.size == 0:
            return "The stack is empty"
        else:
            self.size -= 1
            self.head = self.head.next 

    def delete(self):
        self.head = None 

    
class SetOfStacks:
    def __init__(self, maxStackSize: int):
        self.maxStackSize: int = maxStackSize
        self.stackList: List[Stack] = list()

    def __str__(self):
        s = ""
        for stack in self.stackList:
            print(stack)
            s += str(stack)
        
        return s

    def push(self, value: int):
        if len(self.stackList) == 0:
            stack: Stack = Stack(self.maxStackSize)
            self.stackList.append(stack)
            stack.push(Node(value))
        else:
            stack: Stack = self.stackList[-1]
            if stack.isFull():
                newStack: Stack = Stack(self.maxStackSize)
                newStack.push(Node(value))
                self.stackList.append(newStack)
            else:
                stack.push(Node(value))

    def pop(self):
        if len(self.stackList) == 0:
            return "The set of stacks is empty"
        else:
            stack: Stack = self.stackList[-1]
            value = stack.pop()
            if stack.isEmpty():
                stack.delete()
                del self.stackList[-1]
            return value 

    def popAt(self, index: int):
        if len(self.stackList) == 0:
            return "The stack list is empty"
        else:
            stack: Stack = self.stackList[index]
            return stack.pop()



s = SetOfStacks(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)

    
        

