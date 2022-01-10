# BinaryTreeUsingLinkedList

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

leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tree.leftChild = leftChild
tree.rightChild = rightChild 

# print(tree)

def preOrderTraversal(rootNode): # time O(n), space O(n)
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) # time O(n/2)
    preOrderTraversal(rootNode.rightChild) # time O(n/2)


preOrderTraversal(tree)