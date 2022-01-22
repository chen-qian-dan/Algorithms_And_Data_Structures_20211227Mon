"""
Tree and Graph: 371 - Minimal Tree 
Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height. 


class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):
    # TODO

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minimalTree(sortedArray)

output:
        5
    3       8
  2   4   7  9
1        6
"""

"""
1. problem : 
2. intput: sortedArray
3. output 
4. edge cases:
    empty list
5. time complexity
6. Space complexity 
"""
import math 

sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]

class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root: BSTNode):
        self.root = root 

    def BFSTree(self):
        q = list()
        q.append(self.root)
        while len(q) > 0:
            node = q.pop(0)
            print(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None 
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    
    middle: int = math.floor(len(sortedArray) / 2)
    node = BSTNode(sortedArray[middle])
    node.left = minimalTree(sortedArray[:middle])
    node.right = minimalTree(sortedArray[middle + 1 :])

    return node 


tree = Tree(minimalTree(sortedArray))

tree.BFSTree()