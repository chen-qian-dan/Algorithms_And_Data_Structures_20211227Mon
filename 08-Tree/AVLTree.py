
# AVL Tree

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

    
avl = AVLNode(10)