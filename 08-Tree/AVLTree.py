
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

def searchNode(rootNode, data):
    if not rootNode:
        print("Value not found") 
        return
    if data == rootNode.data:
        print("Value found")
        return  
    elif data < rootNode.data:
        searchNode(rootNode.leftChild, data)
    else:
        searchNode(rootNode.rightChild, data)



def getHeight(rootNode: AVLNode) -> int:
    if not rootNode:
        return 0 

    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild 
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild 
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild 
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0 
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue) 

    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data: # LL condition
        return rightRotate(rootNode)
    elif balance > 1 and nodeValue >= rootNode.leftChild.data: # LR condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    elif balance < -1 and  nodeValue >= rootNode.rightChild.data: # RR condition
        return leftRotate(rootNode)
    elif balance < -1 and  nodeValue < rootNode.rightChild.data: # RL condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode



def getMinValueNode(rootNode):
    if not rootNode or not rootNode.leftChild:
        return rootNode
    return getMinValueNode(rootNode.leftChild)



def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if not rootNode.leftChild:
            temp = rootNode.rightChild
            rootNode = None 
            return temp
        elif not rootNode.rightChild:
            temp = rootNode.leftChild
            rootNode = None 
            return temp 
        else:
            temp = getMinValueNode(rootNode.rightChild)
            rootNode.data = temp.data 
            rootNode.right = deleteNode(rootNode.right, temp.data)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1:
        if getBalance(rootNode.leftChild) >= 0: # LL condition
            return rightRotate(rootNode)
        else:   # LR condition
            rootNode.leftChild = leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)

    if balance < -1:
        if getBalance(rootNode.rightChild) <= 0: # RR condition
            return leftRotate(rootNode)
        else: # RL condition
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)

    return rootNode


def deleteEntireAVLTree(rootNode):
    rootNode.data = None 
    rootNode.leftChild = None 
    rootNode.rightChild = None 
    return "The AVL has been successfully deleted"

                

avl = AVLNode(5)
avl = insertNode(avl, 10)
avl = insertNode(avl, 15)
avl = insertNode(avl, 20)

levelOrderTraverse(avl)
deleteNode(avl, 15)
levelOrderTraverse(avl)
searchNode(avl, 11)