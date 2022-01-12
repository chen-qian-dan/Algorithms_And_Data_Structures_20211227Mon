# Binary Tree using Python List

class BinaryTree:
    def __init__(self, size):
        self.list = [None] * size 
        self.maxSize = size 
        self.lastUsedIndex = 0


bt = BinaryTree(8)