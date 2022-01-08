
# Stack created by Linked List

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class Stack:
    def __init__(self):
        self.head = None 
       
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 

    def __str__(self):
        values = [str(x.value) for x in self] 
        return '->'.join(values)


    def isEmpty(self): # time: O(1), space: O(1)
        return True if self.head is None else False 

    def push(self, value): # time: O(1), space: O(1)
        node = Node(value)
        node.next = self.head 
        self.head = node
        print("Push successfully") 

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
             
        value = self.head.value 
        self.head = self.head.next 
        return value 

        




stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)

print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
