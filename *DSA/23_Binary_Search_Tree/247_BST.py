
from collections import deque 

class Node:
    def __init__(self, val):
        self.val = val 
        self.leftChild = None 
        self.rightChild = None 

def insertNode(root: Node, val): # time O(logN), space O(logN)
    if root is None:
        root = Node(val)
    elif val <= root.val:
        root.leftChild = insertNode(root.leftChild, val)
    else:
        root.rightChild = insertNode(root.rightChild, val)
    return root 


def preOrder_traverse(root: Node) -> list(): # time: O(n), space O(n)
    if root is None:
        return []
    ret = list()
    ret.append(root.val)
    ret.extend(preOrder_traverse(root.leftChild))
    ret.extend(preOrder_traverse(root.rightChild))
    return ret 



root = Node(10)
insertNode(root, 2)
insertNode(root, 3)
insertNode(root, 12)
print(preOrder_traverse(root))
# print(inOrder_traverse(root))