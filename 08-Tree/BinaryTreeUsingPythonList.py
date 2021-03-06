# Binary Tree using Python List

class BinaryTree:
    def __init__(self, size):
        self.list = [None] * size 
        self.maxSize = size 
        self.lastUsedIndex: int = 0


    # insert a node
    # The binary tree is full 
    # we have to look for a first vacant place 
    def insertNode(self, value):
        if self.lastUsedIndex == self.maxSize - 1:
            return "The binary tree is full"
        self.lastUsedIndex += 1
        self.list[self.lastUsedIndex] = value 
        return "The value has been successfully inserted"

    
    def searchNode(self, value):
        for v in self.list:
            if v == value:
                return "Success"
        return "Not found"


    def preOrderTraverse(self, index: int):
        if index > self.lastUsedIndex or index < 1:
            return 
        print(self.list[index])
        self.preOrderTraverse(index * 2)
        self.preOrderTraverse(index * 2 + 1)

    def inOrderTraverse(self, index: int):
        if index > self.lastUsedIndex or index < 1:
            return 
        self.inOrderTraverse(index * 2)
        print(self.list[index])
        self.inOrderTraverse(index * 2 + 1)

    def postOrderTraverse(self, index: int):
        if index > self.lastUsedIndex or index < 1:
            return 
        self.postOrderTraverse(index * 2)
        self.postOrderTraverse(index * 2 + 1)
        print(self.list[index])

    def levelOrderTraverse(self, index: int):
        if index > self.lastUsedIndex or index < 1:
            return 
        for i in range(index, self.lastUsedIndex + 1):
            print(self.list[i])


    def deleteNode(self, value):
        # use the deepest node to replace the node you want to delete
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.maxsize + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex] = None 
                self.lastUsedIndex -= 1
                return "Deleted successfully"
            
        return "There is no such node with that value"


    def deleteEntireBT(self):
        self.list = None 
        return "The entire binary tree is deleted"


    





bt = BinaryTree(8)
"""
            Drinks
        Hot         Cold
    Tea   Coffee
"""
print(bt.insertNode("Drinks"))
print(bt.insertNode("Hot"))
print(bt.insertNode("Cold"))
print(bt.insertNode("Tea"))
print(bt.insertNode("Coffee"))

print(bt.searchNode("Hot"))

# bt.preOrderTraverse(1)
# bt.inOrderTraverse(1)
# bt.postOrderTraverse(1)
bt.levelOrderTraverse(1)
