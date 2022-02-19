
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



tree = Binary_Tree(10)
tree.insertNode(1)
tree.insertNode(2)
tree.insertNode(3)
tree.insertNode(4)
tree.insertNode(5)
print(tree)
