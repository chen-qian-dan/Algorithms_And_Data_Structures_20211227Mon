
# AVL Tree
class QNode:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Queue:
    # enqueue at the end
    # dequeue at the beginning
    def __init__(self):
        self.head = None 
        self.tail = None 

    def enqueue(self, data):
        node = QNode(data)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 

    def dequeue(self):
        if not self.head:
            return "The queue is empty"
        
        data = self.head.data 
        if self.head is self.tail:
            self.head.data = None 
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
        return data 

    def isEmpty(self):
        return True if not self.head else False 





class AVLNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 
        self.height = 1


def preOrderTraverse(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraverse(rootNode.leftChild)
    preOrderTraverse(rootNode.rightChild)

def inOrderTraverse(rootNode):
    if not rootNode:
        return 
    inOrderTraverse(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraverse(rootNode.rightChild)

def postOrderTraverse(rootNode):
    if not rootNode:
        return 
    postOrderTraverse(rootNode.leftChild)
    postOrderTraverse(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraverse(rootNode):
    if not rootNode:
        return 

    q = Queue()
    q.enqueue(rootNode)
    while not q.isEmpty():
        avlNode = q.dequeue()
        print(avlNode.data)
        if avlNode.leftChild:
            q.enqueue(avlNode.leftChild)
        if avlNode.rightChild:
            q.enqueue(avlNode.rightChild)


    
avl = AVLNode(10)

levelOrderTraverse(avl)