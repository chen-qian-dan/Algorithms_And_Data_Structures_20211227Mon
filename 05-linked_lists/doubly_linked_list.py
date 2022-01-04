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

    def traverse(self):
        if self.head is None:
            print("The list is empty ")
            return 
        node: Node = self.head
        while node:
            print(node.value)
            node = node.next

    def traverseReversally(self):
        if not self.head:
            print("The list is empty ")
        else:
            node: Node = self.tail 
            while node:
                print(node.value)
                node = node.pre

    def search(self, value):
        node: Node = self.head
        index = -1
        while node:
            index += 1
            if node.value == value:
                return index 
            else:
                node = node.next
        return False 


    def deleteOneNode(self, location):
        if location < -1 or location > self.count - 1 or not self.head:
            print(f"location is out of range [-1, {self.count - 1}]")
            return 

        if self.head == self.tail: # only one node
            node: Node = self.head
            self.head = None 
            self.tail = None 
            return 

        # delete the first one 
        if location == 0:
            if self.head == self.tail: # only one node
                node: Node = self.head
                self.head = None 
                self.tail = None 
            else: 
                self.head = self.head.next
                self.head.pre.next = None 
                self.head.pre = None 
        # delete the last one
        elif location == -1 or location == self.count - 1:
            if self.head == self.tail: # only one node
                node: Node = self.head
                self.head = None 
                self.tail = None 
            else:
                self.tail = self.tail.pre 
                self.tail.next.pre = None 
                self.tail.next = None 
        # delete the middle one 
        else:
            node: Node = self.head 
            index: int = 0
            while index < location - 1:
                node = node.next
                index += 1
            nodeWantToDelete: Node = node.next
            node.next = nodeWantToDelete.next
            nodeWantToDelete.next.pre = node 
            nodeWantToDelete.next = None 
            nodeWantToDelete.pre = None 
            

    def deleteEntireList(self):
        """
        gabage collection won't collect the node if anyone link to the node
        even is another node link to that node
        So, in order to delete the entire list, need to make every node's pre to be None 
        """
        node: Node = self.head
        while node:
            if node != self.tail:
                node.next.pre = None 
                node = node.next
        self.head = None 
        self.tail = None 

        

            

            



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

# traverse ----------------------------------------------
dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)
dll.insert(2, -1)
dll.insert(3, -1)
dll.traverse()
# dll.traverseReversally()


# search ----------------------------------------------
dll: DoublyLinkedList = DoublyLinkedList()
# dll.append(1)
# dll.insert(2, -1)
# dll.insert(3, -1)
print(dll.search(2))

# delete -----------------------------------------------
dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)

print([node.value for node in dll])
dll.deleteOneNode(0)
print([node.value for node in dll])

# delete the entire list -----------------------------------------------
dll: DoublyLinkedList = DoublyLinkedList()
dll.append(1)
dll.insert(2, -1)
dll.insert(3, -1)
dll.deleteEntireList()
print([node.value for node in dll])
