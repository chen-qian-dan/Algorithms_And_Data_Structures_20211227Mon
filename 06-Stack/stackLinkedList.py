

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()


    def isEmpty(self): # time: O(1), space: O(1)
        return True if self.LinkedList.head is None else False 

    def push(self, value): # time: O(1), space: O(1)
        node = Node(value)
        node.next = self.LinkedList.head 
        self.LinkedList.head = node
        print("Push successfully") 




stack = Stack()
print(stack.isEmpty())
