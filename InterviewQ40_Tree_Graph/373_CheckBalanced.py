"""
The Binary Tree is Balanced if:
1. The right subtree is balanced
2. The left subtree is balanced
3. The different between the height of the left subtree and the right subtree is at most 1
"""





# Balanced Tree

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isBalancedHelper(root):
    if root is None:
        return 0
    leftH = isBalancedHelper(root.left)
    if leftH == -1:
        return -1
    rightH = isBalancedHelper(root.right)
    if rightH == -1:
        return -1
    
    return max(leftH, rightH) + 1

def isBalanced(root):
    return isBalancedHelper(root) > -1



def isBalancedQian2(root):
    # TODO
    if root is None:
        return True
    
    if isBalanced(root.left) is False:
        return False 
    if isBalanced(root.right) is False:
        return False
    
    leftH = getHeight(root.left)
    rightH = getHeight(root.right)

    return False if abs(leftH - rightH) > 1 else True

# Q ---------------------------------------------------------------
def isBalancedQian(root):
    # TODO
    if root is None:
        return True
    # DFSpreOrder
    lst = DFSpreOrder(root)
    for node in lst:
        leftH = getHeight(node.left)
        rightH = getHeight(node.right)
        if abs(leftH - rightH) > 1:
            return False 
    return True
    
    
def getHeight(root):
    if root is  None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))
    
def DFSpreOrder(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root]
    ret = [root]
    left = DFSpreOrder(root.left)
    if left:
        ret.extend(DFSpreOrder(root.left))
    right = DFSpreOrder(root.right)
    if right:
        ret.extend(DFSpreOrder(root.right))
    return ret 
# Q ---------------------------------------------------------------
    
        
