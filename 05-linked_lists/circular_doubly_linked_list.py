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
            return False 

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

        self.count += 1


    def traverse(self):
        node: Node = self.head
        while node:
            print(node.value)
            if node == self.tail:
                break 
            node = node.next

    def traverseReversly(self):
        if not self.head:
            print("The list is empty")
            return 
        node: Node = self.tail
        while node:
            print(node.value)
            if node == self.head:
                break 
            node = node.prev 

    def search(self, value):
        if self.head is None:
            print("There is not any node in the list") 
            return False 
        else:
            node: Node = self.head
            while node:
                if node.value == value:
                    return True 
                elif node == self.tail:
                    return False 
                else:
                    node = node.next

    def deleteOneNode(self, location):
        if not self.head:
            print("Can't delete because the list is empty")
            return False 

        if self.head == self.tail:
            targetNode: Node = self.head
            targetNode.prev = None
            targetNode.next = None 
            self.head = None 
            self.tail = None 
        elif location == 0:
            targetNode: Node = self.head
            self.head = targetNode.next
            self.tail.next = self.head
            self.head.prev = self.tail
           
        elif location == -1 or location == self.count - 1:
            targetNode: Node = self.tail
            self.tail = targetNode.prev 
            self.tail.next = self.head
            self.head.prev = self.tail
            
        else:
            index: int = 0
            targetNode: Node = self.head
            while index < location:
                index += 1
                targetNode = targetNode.next
            targetNode.prev.next = targetNode.next
            targetNode.next.prev = targetNode.prev 
            

        self.count -= 1

        return True 

    
    def deleteEntireList(self):
        if not self.head:
            print("The list is empty already")
            return False 
        else:
            node: Node = self.head
            # make it non circular first
            self.tail.next = None
            while node:
                node.prev = None 
                node = node.next
            self.head = None 
            self.tail = None 
            return True 






# create -------------------------------------
# cdll: CircularDoublyLinkedList = CircularDoublyLinkedList()
# cdll.create(1)
# print([node.value for node in cdll])


# insert -------------------------------------
cdll: CircularDoublyLinkedList = CircularDoublyLinkedList()
cdll.create(1)
cdll.insert(0, location = -1)
cdll.insert(2, location = 1)
# print([node.value for node in cdll])

# cdll.insert(3, location = 2)

print([node.value for node in cdll])
# cdll.traverse()
# cdll.traverseReversly()
# print(cdll.search(-11))
cdll.deleteOneNode(2)
print([node.value for node in cdll])
cdll.deleteEntireList()
print([node.value for node in cdll])