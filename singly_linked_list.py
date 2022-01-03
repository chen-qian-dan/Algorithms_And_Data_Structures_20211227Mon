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





print([node.value for node in singlyLinkedList])

# node = singlyLinkedList.head
# while node:
#     print(node.value)
#     node = node.next