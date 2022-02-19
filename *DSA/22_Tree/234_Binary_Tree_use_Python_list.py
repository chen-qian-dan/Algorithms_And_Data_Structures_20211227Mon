
from re import search


class Binary_Tree:
    """
    1. Fixed size python list
    2. lastUsedIndex
    3. cell 0 is not used
    """
    def __init__(self, capacity: int): # time O(1), space O(n)
        self.items = [None] * capacity 
        self.lastUsedIndex = 0
        self.capacity = capacity 

    def __str__(self):
        return str(self.items)

    def insertNode(self, val): # time O(1), space O(1)
        """
        1. the binary tree is full
        2. find a first vacant place 
        """
        if self.lastUsedIndex == self.capacity - 1:
            print("The tree is full")
        self.lastUsedIndex += 1
        self.items[self.lastUsedIndex] = val 


    def searchNode(self, val): # time O(n), space O(1)
        if self.lastUsedIndex == 0:
            print("The tree is empty")
        else:
            for i in range(1, self.lastUsedIndex + 1):
                if self.items[i] == val:
                    print(i)
                    return 
            print("The val is not in the tree") 

    
    def preOrder_traverse(self, rootIndex: int) -> list(): # time O(n), space O(n)
        if rootIndex > self.lastUsedIndex:
            return []
        ret = list()
        ret.append(self.items[rootIndex])
        ret.extend(self.preOrder_traverse(rootIndex * 2))
        ret.extend(self.preOrder_traverse(rootIndex * 2 + 1))
        return ret 


    def inOrder_traverse(self, rootIndex: int) -> list(): # time O(n), space O(n)
        if rootIndex > self.lastUsedIndex:
            return []
        ret = list()
        ret.extend(self.inOrder_traverse(rootIndex * 2))
        ret.append(self.items[rootIndex])
        ret.extend(self.inOrder_traverse(rootIndex * 2 + 1))
        return ret 

    def postOrder_traverse(self, rootIndex: int) -> list(): # time O(n), space O(n)
        if rootIndex > self.lastUsedIndex:
            return [] 
        ret = list()
        ret.extend(self.postOrder_traverse(rootIndex * 2))
        ret.extend(self.postOrder_traverse(rootIndex * 2 + 1))
        ret.append(self.items[rootIndex])
        return ret 

    def levelOrder_traverse(self, rootIndex: int) -> list(): # time O(n), space O(n)
        if rootIndex > self.lastUsedIndex:
            return [] 
        return self.items[rootIndex: self.lastUsedIndex+1] # by val 

    
    def deleteNode(self, val) -> None: # time O(n), space O(1)
        if self.lastUsedIndex == 0:
            print("The tree is empty")
        else:
            bExist = False 
            for i in range(1, self.lastUsedIndex + 1):
                if self.items[i] == val:
                    self.items[i] = self.items[self.lastUsedIndex]
                    self.items[self.lastUsedIndex] = None 
                    bExist = True 
                    self.lastUsedIndex -= 1
                    break 

            if bExist is False:
                print("The val is not in the tree")
            else:
                print("Delete it successfully")

        



tree = Binary_Tree(10)
tree.insertNode(1)
tree.insertNode(2)
tree.insertNode(3)
tree.insertNode(4)
tree.insertNode(5)
print(tree)
tree.searchNode(1)

# print(tree.preOrder_traverse(1))
# print(tree.inOrder_traverse(1))
# print(tree.postOrder_traverse(1))
print(tree.levelOrder_traverse(1))
tree.deleteNode(6)
print(tree.levelOrder_traverse(1))

