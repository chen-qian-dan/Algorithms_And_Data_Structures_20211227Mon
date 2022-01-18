# Fractional Knapsack Problem

from typing import List 

class Item:
    def __init__(self, weight: float, value: float):
        self.weight: float = weight
        self.value: float = value
        self.ratio: float = value / weight

    

def findMaxValueBasedLimitWeight(items: List[Item], weightLimit: float): # ------ time: O(NlogN), space: O(1)
    """
    print total weight, total value
    """
    items.sort(key = lambda x: x.ratio, reverse = True) # ------ time: O(NlogN)
    totalWeight: float = 0.0
    totalValue: float = 0.0

    for item in items: # ------------- time: O(N)
        weightCapacity = weightLimit - totalWeight
        count = weightCapacity / item.weight
        if count > 1:
            count = 1
        totalValue += item.value * count 
        totalWeight += item.weight * count 
        if totalWeight == weightLimit:
            break 

    print(f"totalValue = {totalValue}, totalWeight = {totalWeight}")



item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)

items = [item1, item2, item3]

findMaxValueBasedLimitWeight(items, 50)



