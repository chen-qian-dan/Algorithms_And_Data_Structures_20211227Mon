from collections import deque 


class Node:
    def __init__(self, val):
        self.val = val 
        self.leftChild = None 
        self.rightChild = None 


def preOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return None 
    ret = [node.val]
    ret.extend(preOrder_traverse(node.leftChild)) # time O(n/2)
    ret.extend(preOrder_traverse(node.rightChild)) # time O(n/2)
    return ret 

def inOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return None
    ret = inOrder_traverse(node.leftChild) # time O(n/2)
    ret.append(node.val)
    ret.extend(inOrder_traverse(node.rightChild)) # time O(n/2)
    return ret 

def postOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return None
    ret = postOrder_traverse(node.leftChild) # time O(n/2)
    ret.extend(postOrder_traverse(node.rightChild)) # time O(n/2)
    ret.append(node.val)
    return ret 


def levelOrder_traverse(node: Node): # time O(n), space O(n)
    if node is None:
        return None 
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


def insertNode(root: Node, val): # by ref
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

    return root 



def deleteNode(root: Node, val):
    if root is None:
        print("The tree is empty")
        return None 
   
    bExist = False 
    deepestNoded = getDeepestNode(root)
    newRoot = Node(None)
    newRoot.leftChild = root 
    q = deque()
    q.append(newRoot)
    while len(q) > 0:
        node = q.popleft()
        if node.leftChild:
            if node.leftChild.val == val:
                node.leftChild.val = deepestNoded.val
                bExist = True
                break 
            else:
                q.append(node.leftChild)
        if node.rightChild:
            if node.rightChild.val == val:
                node.rightChild.val = deepestNoded.val
                bExist = True 
                break 
            else:
                q.append(node.rightChild)
    if not bExist:
        print("The val is not in the tree")
        return None 
                
    root = deleteDeepestNode(newRoot.leftChild)

    return root 


def deleteDeepestNode(root: Node):
    if root is None:
        return None

    deepestNode = getDeepestNode(root)
    newRoot = Node(0)
    newRoot.leftChild = root 
    q = deque()
    q.append(newRoot)
    while len(q) > 0:
        node = q.popleft()
        if node.val == 3:
            print("")
        if node.leftChild:
            if node.leftChild is deepestNode:
                node.leftChild = None 
                break 
            else:
                q.append(node.leftChild)
        if node.rightChild:
            if node.rightChild is deepestNode:
                node.rightChild = None 
                break 
            else:
                q.append(node.rightChild)
    return newRoot.leftChild



def getDeepestNode(root: Node):
    if root is None:
        return None 
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        if node.leftChild:
            q.append(node.leftChild)
        if node.rightChild:
            q.append(node.rightChild)
    return node


def deleteTree(root: Node): 
    """
    root = None 
    root.leftChild = None 
    root.rightChild = None
    """ 
    root.leftChild = None
    root.rightChild = None 
    root.val = None 
    return None 


root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root = insertNode(root, 4)
root = insertNode(root, 5)
root = insertNode(root, 6)

print(levelOrder_traverse(root))
root = deleteNode(root, 1)
print(levelOrder_traverse(root))
# root = deleteTree(root)
# print(levelOrder_traverse(root))

# print(inOrder_traverse(root))
# print(postOrder_traverse(root))
# print(levelOrder_traverse(root))

# print(searchNode(root, Node(20)))

root = insertNode(root, 20)
# print(levelOrder_traverse(root))


