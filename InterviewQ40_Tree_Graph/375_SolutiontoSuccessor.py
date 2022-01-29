#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Validate BST

class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node


def inOrderSuccessor(root, n):
    # TODO
    """
    if the root.right is NOT NONE, then the successor is in the right subtree
    if the root.right is NONE, then the successor is one of the ancestor 
    """
    if root.right is None:
        parent = root.parent
        if parent is None:
            return None 
        if root is parent.left:
            return parent 
        if root is parent.right:
            gran = parent.parent
            if gran and parent is gran.left:
                return gran
            else:
                return None 






