"""
449_Singly Linked List - Rotate
The function should rotate all the nodes in the list by some number passed in. 
For instance, 
If your list looks like 
1 -> 2 -> 3 -> 4 -> 5 and you rotate by 2, the list should be modified to 
3 -> 4 -> 5 -> 1 -> 2

The number passed in to rotate can be any integer. 
Time complexity: O(N)
Space Complexity: O(1)


singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)    # Success
singlyLinkedList.push(10)    # Success
singlyLinkedList.push(15)    # Success
singlyLinkedList.push(20)    # Success
singlyLinkedList.push(25)    # Success

singlyLinkedList.rotate(3)
singlyLinkedList.head.val   # 20
singlyLinkedList.head.next.val   # 25
singlyLinkedList.head.next.next.val   # 5
singlyLinkedList.head.next.next.next.val   # 10
singlyLinkedList.head.next.next.next.next.val   # 15
singlyLinkedList.tail.val   # 15
singlyLinkedList.tail.next   # None

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(5)    # Success
singlyLinkedList.push(10)    # Success
singlyLinkedList.push(15)    # Success
singlyLinkedList.push(20)    # Success
singlyLinkedList.push(25)    # Success

singlyLinkedList.rotate(-1)
singlyLinkedList.head.val   # 25
singlyLinkedList.head.next.val   # 5
singlyLinkedList.head.next.next.val   # 10
singlyLinkedList.head.next.next.next.val   # 15
singlyLinkedList.head.next.next.next.next.val   # 20
singlyLinkedList.tail.val   # 20
singlyLinkedList.tail.next   # None



# Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
        
    def rotate(self, number):
        # TODO

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
        
    def rotate(self, number):
        # TODO
        if self.length == 0 or self.length == 1:
            return 
        if number >= self.length:
            number = self.length - 1 

        elif number < - 1 * self.length:
            number = 0 

        elif number >= - 1 * self.length and number < 0:
            number = self.length + number
        
        if number == 0:
            return 
        for i in range(number):
            # pop(0) and push at the end
            node = self.head
            self.head = self.head.next
            self.tail.next = node 
            self.tail = node 
            self.tail.next = None 
         


singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))    # Success
print(singlyLinkedList.push(10))    # Success
print(singlyLinkedList.push(15))    # Success
print(singlyLinkedList.push(20))    # Success
print(singlyLinkedList.push(25))    # Success

print(singlyLinkedList.rotate(3))
print(singlyLinkedList.head.val)   # 20
print(singlyLinkedList.head.next.val)   # 25
print(singlyLinkedList.head.next.next.val)   # 5
print(singlyLinkedList.head.next.next.next.val)   # 10
print(singlyLinkedList.head.next.next.next.next.val)   # 15
print(singlyLinkedList.tail.val)   # 15
print(singlyLinkedList.tail.next)   # None

singlyLinkedList = SinglyLinkedList()
print(singlyLinkedList.push(5))    # Success
print(singlyLinkedList.push(10))    # Success
print(singlyLinkedList.push(15))    # Success
print(singlyLinkedList.push(20))    # Success
print(singlyLinkedList.push(25))    # Success

singlyLinkedList.rotate(-1)
print(singlyLinkedList.head.val)   # 25
print(singlyLinkedList.head.next.val)   # 5
print(singlyLinkedList.head.next.next.val)   # 10
print(singlyLinkedList.head.next.next.next.val)   # 15
print(singlyLinkedList.head.next.next.next.next.val)   # 20
print(singlyLinkedList.tail.val)   # 20
print(singlyLinkedList.tail.next)   # None
