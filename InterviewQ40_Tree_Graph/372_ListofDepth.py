#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# List of Depth
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree == None:
        return 0
    if tree.left == None  and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight

def treeToLinkedList(tree, custDict = {}, d = None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict


def treeToLinkedListQian(root, level = None):
    # TODO
    custDict = {}
    if root is None:
        return None
    if level is None:
        level = depth(root)
    if level < 1:
        return None 
        
    q = list()
    q.append(root)
    for i in range(level):
        temp = list()
        ll = LinkedList(None)
        curNode = ll
        while len(q) > 0:
            node = q.pop(0)
            curNode.next = LinkedList(node.val)
            curNode = curNode.next 
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        q = temp
        ll = ll.next 
        custDict[i+1] = ll
    return custDict

mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
print(custDict[3])
print(custDict[2])
print(custDict[1])
# for depthLevel, linkedList in custDict.items():
#     print("{0} {1}".format(depthLevel, linkedList))

print("Q ----------------------------")
a = treeToLinkedListQian(mainTree)
for e in a.keys():
    print(a[e])

print(a[1])