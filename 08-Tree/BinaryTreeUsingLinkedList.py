# BinaryTreeUsingLinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def isEmpty(self):
        return True if not self.head else False 

    def create(self, data):
        if not self.head:
            print ("The queue is not empty, need to call empty before create")
            return 
        node = Node(data)
        self.head = node
        self.tail = node 

    def enqueue(self, data):
        # add at tail, remove at head 
        node = Node(data)
        if self.isEmpty():
            self.head = node 
            self.tail = node 

        else:
            self.tail.next = node 
            self.tail = node 

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        value = self.head.data
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
        return value 



# Create
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None 
        self.rightChild = None 

    def __str__(self):
        level = 0 
        ret = "   " * level + str(self.data) + "\n"
        if self.leftChild:
            ret += "   " * (level + 1) + self.leftChild.__str__()
        else:
            ret += "\n"
        if self.rightChild:
            ret += "   " * (level + 1) + self.rightChild.__str__()
        else:
            ret += "\n"
        return ret 

    
tree = TreeNode("Drinks")

hot = TreeNode("Hot")
cold = TreeNode("Cold")

tea = TreeNode("Tea")

tree.leftChild = hot
tree.rightChild = cold
hot.leftChild = tea 

# print(tree)

def preOrderTraversal(rootNode): # time O(n), space O(n)
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) # time O(n/2)
    preOrderTraversal(rootNode.rightChild) # time O(n/2)


# preOrderTraversal(tree)

def inOrderTraversal(rootNode): # time O(n), space(n)
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild) # time O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild) # time O(n/2)

# inOrderTraversal(tree)


def postOrderTraversal(rootNode): # time O(n), space(n)
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild) # time O(n/2)
    postOrderTraversal(rootNode.rightChild) # time O(n/2)
    print(rootNode.data)

# postOrderTraversal(tree)


def levelOrderTraversal(rootNode):
    # need a queue
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

levelOrderTraversal(tree)

def searchANodeInBinaryTree(rootNode, data) -> bool:
    if not rootNode:
        print("The tree is empty")
        return False 
    
    q = Queue()
    q.enqueue(rootNode)
    while not q.isEmpty():
        node = q.dequeue()
        if node.data == data:
            return True 
        if node.leftChild:
            q.enqueue(node.leftChild)
        if node.rightChild:
            q.enqueue(node.rightChild)
    return False 

print(searchANodeInBinaryTree(tree, "Tea"))


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode 
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            treeNode = q.dequeue()
            if not treeNode.leftChild:
                treeNode.leftChild = newNode
                break 
            q.enqueue(treeNode.leftChild)
            if not treeNode.rightChild:
                treeNode.rightChild = newNode
                break
            q.enqueue(treeNode.rightChild)
        print("Insert successfully")


colar = TreeNode("Colar")
insertNodeBT(tree, colar)
levelOrderTraversal(tree)
                 
            




    

