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
            self.insertNode(root.leftChild, data)
    else:
        if not root.rightChild:
            root.rightChild = newNode 
        else:
            self.insertNode(root.rightChild, data)

    return "Insert successfully"



newBTS = BSTNode(None)
insertNode(newBTS, 70)
insertNode(newBTS, 50)
print(newBTS.data)
print(newBTS.leftChild.data)