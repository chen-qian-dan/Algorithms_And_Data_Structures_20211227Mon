# Doubly Linked List

# create -----------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value 
        self.pre = None 
        self.next = None 
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.count = 0


    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next

    def append(self, value):
        node: Node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            node.prev = self.tail 
            self.tail.next = node 
            self.tail = node 
        self.count += 1

    def insert(self, value, location: int):
        node: Node = Node(value)
        if location < -1 or location > self.count:
            print("location is out of range [0, {self.count}]")
            return False 
        # if list is empty
        if not self.head:
            self.head = node 
            self.tail = node 
        # insert at the beginning
        elif location == 0:
            node.next = self.head
            self.head.pre = node 
            self.head = node 
        # insert at the end 
        elif location == -1 or location == self.count:
            node.pre = self.tail 
            self.tail.next = node
            self.tail = node 
        # insert in the middle 
        else:
            index: int = 0
            curNode: Node = self.head 
            while index < location - 1:
                curNode = curNode.next 
                index += 1
            node.next = curNode.next 
            curNode.next.pre = node 
            node.pre = curNode 
            curNode.next = node 

        self.count += 1 
        return True 
            



dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)
dll.append(2)
print([node.value for node in dll])


# insert -----------------------------------------------
dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)
print([node.value for node in dll])
dll.insert(2, -1)
dll.insert(3, -1)
print([node.value for node in dll])
