class Item: 
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value 
        self.ratio = self.value / self.weight


def snapsackMethod(items, weightLimit):  # time O(NlogN + N)
    items.sort(key = lambda x: x.ratio, reverse = True) # time O(NlogN)
    usedCapacity = 0
    totalValue = 0
    for i in items: # time O(N)
        if weightLimit - usedCapacity >= i.weight:
            usedCapacity += i.weight
            totalValue += i.value 
        elif weightLimit - usedCapacity > 0:
            weight = weightLimit - usedCapacity
            usedCapacity += weight
            totalValue += i.ratio * weight
        else:
            break 
    return totalValue


   



item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)

items = [item1, item2, item3]

print(snapsackMethod(items, 50))