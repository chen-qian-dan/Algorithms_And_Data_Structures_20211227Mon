from collections import deque 


class Node:
    def __init__(self, val):
        self.val = val 
        self.leftChild = None 
        self.rightChild = None 


def preOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return [] 
    ret = [node.val]
    ret.extend(preOrder_traverse(node.leftChild)) # time O(n/2)
    ret.extend(preOrder_traverse(node.rightChild)) # time O(n/2)
    return ret 

def inOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return []
    ret = inOrder_traverse(node.leftChild) # time O(n/2)
    ret.append(node.val)
    ret.extend(inOrder_traverse(node.rightChild)) # time O(n/2)
    return ret 

def postOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return []
    ret = postOrder_traverse(node.leftChild) # time O(n/2)
    ret.extend(postOrder_traverse(node.rightChild)) # time O(n/2)
    ret.append(node.val)
    return ret 


def levelOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return []
    ret = deque()
    q = deque() 
    q.append(node)
    while len(q) > 0:
        n = q.popleft()
        ret.append(n.val)
        if n.leftChild is not None:
            q.append(n.leftChild)
        if n.rightChild is not None:
            q.append(n.rightChild)
        
    return list(ret)


def searchNode(root: Node, node: Node) -> bool:
    if root is None:
        return False 
    q = deque()
    q.append(root)
    while len(q) > 0:
        n = q.popleft()
        if n.val == node.val:
            return True 
        if n.leftChild:
            q.append(n.leftChild)
        if n.rightChild:
            q.append(n.rightChild)
    return False 


def insertNode(root: Node, val):
    newNode = Node(val)
    if root is None:
        root = newNode
    else:
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            if node.leftChild is None:
                node.leftChild = newNode 
                break 
            else:
                q.append(node.leftChild)
            if node.rightChild is None:
                node.rightChild = newNode 
                break 
            else:
                q.append(node.rightChild)







root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
print(preOrder_traverse(root))
print(inOrder_traverse(root))
print(postOrder_traverse(root))
print(levelOrder_traverse(root))

print(searchNode(root, Node(20)))

insertNode(root, 20)
print(levelOrder_traverse(root))


