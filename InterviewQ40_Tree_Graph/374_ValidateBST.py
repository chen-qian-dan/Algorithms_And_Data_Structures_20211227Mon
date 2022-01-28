


# class TreeNode:
#      def __init__(self, value):
#          self.val = value
#          self.left = None
#          self.right = None


# def isValidBST(root):
#     # TODO
#     # if left subtree is BST
#     # if right subtree is BST
#     # if leftChild < root < rightChild
#     if root is None:
#         return True 
#     if root.left is None and root.right is None:
#         return True 
#     if isValidBST(root.left) is False:
#         return False 
#     if isValidBST(root.right) is False:
#         return False 
#     if root.left and root.left.val > root.val:
#         return False 
#     if root.right and root.right.val < root.val:
#         return False 
#     return True 

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # TODO
        # if left subtree is BST
        # if right subtree is BST
        # if leftChild < root < rightChild (doesn't work)
        """
        5
      2   9
         1  10
    It meets all the requirement but is not a BST
    so, the requirement should be:
    1. left subtree is BST
    2. right subtree is BST
    3. all left nodes < root < all right nodes
     """
        # if root is None:
        #     return True 
        # if root.left is None and root.right is None:
        #     return True 
        # if self.isValidBST(root.left) is False:
        #     return False 
        # if self.isValidBST(root.right) is False:
        #     return False 
        # if root.left and root.left.val >= root.val:
        #     return False 
        # if root.right and root.right.val <= root.val:
        #     return False 
        # return True 
        # # wrong, failed in leetcode 

        if root is None:
            return True 
        if root.left and root.left.val >= root.val:
            return False 
        if root.right and root.right.val <= root.val:
            return False 
        if isValidBST(root.left) is False:
            return False
        if isValidBST(root.right) is False:
            return False 

    # def isAllLeftNodesSmaller(self, root):
    #     if root is None:
    #         return True 
    #     if root.left and root.left.val >= root.val:
    #         return False 
    #     if root.right and root.right.val <= root.val:
    #         return False 
    #     if isAllLeftNodesSmaller(root.left) is False:
    #         return False
    #     if isAllLeftNodesSmaller(root.right) is False:
    #         return False 
        

node1 = TreeNode(0)
node2 = TreeNode(-1)
node1.left = node2
s = Solution()
print(s.isValidBST(node1))

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(6)
n4 = TreeNode(3)
n5 = TreeNode(7)

n1.left = n2

n2.left = n3
n2.right = n4

n4.left = n5

print(s.isValidBST(n1)) # expected False

