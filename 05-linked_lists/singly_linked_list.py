# Singly Linked List
# creation

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    # insertion
    def insert(self, value, location: int):
        nodeNew: Node = Node(value = value)
        if self.head is None:
            self.head = nodeNew
            self.tail = nodeNew
        else: 
            if location == 0:           # head
                nodeNew.next = self.head
                self.head = nodeNew
            elif location == -1:        # tail
                self.tail.next = nodeNew
                self.tail = nodeNew
            else:                       # middle
                tmpNode = self.head
                index: int = 0
                while index < location - 1:
                    tmpNode = tmpNode.next
                    index += 1

                nodeNew.next = tmpNode.next
                tmpNode.next = nodeNew


    # delete a node
    def deleteNode(self, location):
        if self.head is None:
            print("The list is empty")
            return 

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                self.head = self.head.next

        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None 
            else:
                node: Node = self.head
                
                while node.next is not None and node.next != self.tail:
                    node = node.next
                
                self.tail = node
                node.next = None 
        else:
            node: Node = self.head
            index: int = 0
            while index < location - 1 and node.next:
                index += 1
                node = node.next
            
            if node.next is None:
                print("The location is out of range")
            else: 
                node.next = node.next.next 

            
    # delete the entire list
    def deleteEntireList(self):
        self.head = None 
        self.tail = None 


    # traverse
    def traverse(self):
        if not self.head:
            print("The list is empty")
            return 

        node: Node = self.head
        while node:
            print(node.value)
            node = node.next


    # search
    def search(self, value):
        if self.head is None:
            return False
        node: Node = self.head
        index: int = 0
        while node.value != value and node.next:
            node = node.next
            index += 1

        if node.value == value:
            return index
        return False 

        

singlyLinkedList: SinglyLinkedList = SinglyLinkedList()
# node1: Node = Node(1)
# node2: Node = Node(2)


# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2


singlyLinkedList.insert(1, -1)
singlyLinkedList.insert(2, -1)
singlyLinkedList.insert(3, -1)
singlyLinkedList.insert(4, 0)



# singlyLinkedList.traverse()
# print(singlyLinkedList.search(20))

# print([node.value for node in singlyLinkedList])
# print(singlyLinkedList.deleteNode(-1))
# print([node.value for node in singlyLinkedList])


print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteEntireList()
print([node.value for node in singlyLinkedList])


# node = singlyLinkedList.head
# while node:
#     print(node.value)
#     node = node.next