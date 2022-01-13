# Binary Search Tree Using Linked List

class QNode:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Queue:
    # insert at the end
    # remove at the beginning
    def __init__(self):
        self.head = None 
        self.tail = None 

    def enqueue(self, data):
        node =QNode(data)
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            self.tail = node 

    def dequeue(self):
        if not self.head:
            return "The queue is empty"
        elif self.head == self.tail:
            data = self.head.data
            self.head = None 
            self.tail = None 
            return data 
        else:
            data = self.head.data
            self.head = self.head.next 
            return data 

    def isEmpty(self):
        return True if not self.head else False 





# create
class BSTNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 


def insertNode(root, data):
    if not root:
        root = BSTNode(data)
    
    if not root.data:
        root.data = data
        return "Insert successfully"
    
    newNode = BSTNode(data)

    if data <= root.data:
        if not root.leftChild:
            root.leftChild = newNode 
        else:
            insertNode(root.leftChild, data)
    else:
        if not root.rightChild:
            root.rightChild = newNode 
        else:
            insertNode(root.rightChild, data)

    return "Insert successfully"


def preOrderTraverse(rootNode: BSTNode):
    if not rootNode:
        return 

    print(rootNode.data)
    if rootNode.leftChild:
        preOrderTraverse(rootNode.leftChild)

    if rootNode.rightChild:
        preOrderTraverse(rootNode.rightChild)

def inOrderTraverse(rootNode: BSTNode):
    if not rootNode:
        return 
    
    inOrderTraverse(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraverse(rootNode.rightChild)

def postOrderTraverse(rootNode: BSTNode):
    if not rootNode:
        return 
    postOrderTraverse(rootNode.leftChild)
    postOrderTraverse(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraverse(rootNode: BSTNode):
    if not rootNode:
        return 

    q = Queue()
    q.enqueue(rootNode)
    while not q.isEmpty():
        node = q.dequeue()
        print(node.data)
        if node.leftChild:
            q.enqueue(node.leftChild)
        if node.rightChild:
            q.enqueue(node.rightChild)


def searchNode(rootNode: BSTNode, data):
    if not rootNode:
        print("Not Found")
    elif data == rootNode.data:
        print("Found")
    elif data < rootNode.data:
        searchNode(rootNode.leftChild, data)
    else:
        searchNode(rootNode.rightChild, data)



newBTS = BSTNode(None)
insertNode(newBTS, 70)
insertNode(newBTS, 50)
insertNode(newBTS, 90)
insertNode(newBTS, 30)
insertNode(newBTS, 60)
insertNode(newBTS, 80)
insertNode(newBTS, 100)
insertNode(newBTS, 20)
insertNode(newBTS, 40)
# print(newBTS.data)
# print(newBTS.leftChild.data)

# preOrderTraverse(newBTS)
# inOrderTraverse(newBTS)
# postOrderTraverse(newBTS)
# levelOrderTraverse(newBTS)

searchNode(newBTS, 98)