
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


tree = Binary_Tree(10)
print(tree)
