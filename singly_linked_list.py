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


singlyLinkedList: SinglyLinkedList = SinglyLinkedList()
node1: Node = Node(1)
node2: Node = Node(2)


singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

# insertion
# insert a new node at the beginning

# insert a new node after a node

# insert a new node at the end


for node in singlyLinkedList:
    print(node.value)

# node = singlyLinkedList.head
# while node:
#     print(node.value)
#     node = node.next