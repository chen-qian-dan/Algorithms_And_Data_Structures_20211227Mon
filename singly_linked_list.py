# creation

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None 


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 


singlyLinkedList: SinglyLinkedList = SinglyLinkedList()
node1: Node = Node(1)
node2: Node = Node(2)


singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

