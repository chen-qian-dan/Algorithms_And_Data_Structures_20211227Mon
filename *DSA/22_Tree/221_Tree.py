

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.children = list()

    def __str__(self, level = 0):
        ret = "   " * level + str(self.val) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret 

    def addChild(self, node):
        self.children.append(node)



tree = TreeNode("Drinks")
cold = TreeNode("Cold")
hot = TreeNode("Hot")
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")

cold.addChild(cola)
cold.addChild(fanta)

hot.addChild(tea)
hot.addChild(coffee)

print(tree)