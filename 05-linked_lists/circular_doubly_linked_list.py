# Circular Doubly Linked List


# create -------------------------------------
class Node:
    def __init__(self, value):
        self.value = value 
        self.prev = None 
        self.next = None 

class CircularDoublyLinkedList:

    def __init__(self):
        self.count: int = 0
        self.head = None 
        self.tail = None 
        

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            if node == self.tail:
                break 
            node = node.next 

    def create(self, value):
        node: Node = Node(value)
        self.head = node 
        self.tail = node
        node.next = node 
        node.prev = node 
        self.count += 1
        print("Create successfully")


    def insert(self, value, location: int):
        if self.head is None:
            print("the list is not cated yet.")

        if location < -1 or location > self.count + 1:
            print(f"location is out of range [-1, {self.count}]")
            return False 

        node: Node = Node(value)
        # insert at the beginning 
        if location == 0:
            node.next = self.head 
            self.head.prev = node
            self.head = node 

            self.tail.next = node 
            node.prev = self.tail 
        # insert at the end 
        elif location == -1 or location == self.count:
            node.prev = self.tail 
            self.tail.next = node
            node.next = self.head 
            self.head.prev = node 
            self.tail = node 
        
        # insert in the middle 
        else:
            tmpNode: Node = self.head 
            index = 0
            while index < location - 1:
                tmpNode = tmpNode.next
                index += 1
            node.next = tmpNode.next 
            node.prev = tmpNode 
            tmpNode.next.prev = node 
            tmpNode.next = node 


    def traverse(self):
        node: Node = self.head
        while node:
            print(node.value)
            if node == self.tail:
                break 
            node = node.next




# create -------------------------------------
# cdll: CircularDoublyLinkedList = CircularDoublyLinkedList()
# cdll.create(1)
# print([node.value for node in cdll])


# insert -------------------------------------
cdll: CircularDoublyLinkedList = CircularDoublyLinkedList()
cdll.create(1)
cdll.insert(0, location = -1)
cdll.insert(2, location = 1)
print([node.value for node in cdll])

cdll.insert(3, location = 2)

print([node.value for node in cdll])
# cdll.traverse()


 