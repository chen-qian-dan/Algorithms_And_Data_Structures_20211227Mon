"""
Singly Linked List - Push
This function should take in a value and add a node to the end of the SinglyLinkedList. 
It should return the SinglyLinkedList. 

Example:
singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)    # Success
singlyLinkedList.length     # 1
singlyLinkedList.head.val   # 5
singlyLinkedList.tail.val   # 5

singlyLinkedList.push(10)   # Success
singlyLinkedList.length     # 2
singlyLinkedList.head.val   # 5
singlyLinkedList.head.next.val  # 10
singlyLinkedList.tail.val   # 10


singlyLinkedList.pop().val  # 10
singlyLinkedList.tail.val   # 5
singlyLinkedList.length     # 1
singlyLinkedList.pop().val  # 5
singlyLinkedList.length     # 0
singlyLinkedList.pop()      # Undefined

1. problem
2. input
3. output
4. edge cases
5. time complexity
6. space complexity
"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0

    def push(self, value): # push at the end
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            self.tail = node 

        self.length += 1
        print("Success")

    def pop(self): # pop at the end 
        if self.length == 0:
            return "Undefined"
        # if self.length == 1:
        #     node = self.tail 
        #     self.head = None 
        #     self.tail = None 
        #     self.length -= 1
        #     return node 
        # else:
        retNode = self.tail 
        node = self.head 
        while node.next is not self.tail and node.next is not None:
            node = node.next 
        node.next = None 
        self.tail = node 
        self.length -= 1
        return retNode
            


singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)    # Success
print(singlyLinkedList.length)     # 1
print(singlyLinkedList.head.val)   # 5
print(singlyLinkedList.tail.val)   # 5

singlyLinkedList.push(10)   # Success
print(singlyLinkedList.length)     # 2
print(singlyLinkedList.head.val)   # 5
print(singlyLinkedList.head.next.val)  # 10
print(singlyLinkedList.tail.val)  # 10

print("-----------------------------------")
print(singlyLinkedList.pop().val)  # 10
print(singlyLinkedList.tail.val)   # 5
print(singlyLinkedList.length)     # 1
print(singlyLinkedList.pop().val)  # 5
print(singlyLinkedList.length)     # 0
print(singlyLinkedList.pop())      # Undefined


            
