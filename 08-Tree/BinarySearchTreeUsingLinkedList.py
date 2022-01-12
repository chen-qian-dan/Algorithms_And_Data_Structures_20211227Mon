# Binary Search Tree Using Linked List



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

preOrderTraverse(newBTS)