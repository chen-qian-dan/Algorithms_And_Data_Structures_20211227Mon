
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


def inOrder_traverse(root: Node) -> list(): # time: O(n), space O(n)
    if root is None:
        return []
    ret = list()
    ret.extend(inOrder_traverse(root.leftChild))
    ret.append(root.val)
    ret.extend(inOrder_traverse(root.rightChild))
    return ret 

def postOrder_traverse(root: Node) -> list(): # time: O(n), space O(n)
    if root is None:
        return []
    ret = list()
    ret.extend(postOrder_traverse(root.leftChild))
    ret.extend(postOrder_traverse(root.rightChild))
    ret.append(root.val)
    return ret 

def levelOrder_traverse(root: Node) -> list(): # time: O(n), space O(n)
    if root is None:
        return []
    ret = list()
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        ret.append(node.val)
        if node.leftChild:
            q.append(node.leftChild)
        if node.rightChild:
            q.append(node.rightChild)
    return ret 




root = Node(10)
insertNode(root, 2)
insertNode(root, 3)
insertNode(root, 12)
print(preOrder_traverse(root))
print(inOrder_traverse(root))
print(postOrder_traverse(root))
print(levelOrder_traverse(root))