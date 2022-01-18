# Coin Change Problem

from typing import List
from copy import deepcopy

def getMinCoinChanges(amount: int, coins: List[int]): # ------ time O(N^2)? space O(1)
    denominations = deepcopy(coins)
    denominations.sort(reverse = True)
    count: int = 0 

    while amount > 0:
        coinIndex = 0
        while denominations[coinIndex] > amount:
            coinIndex += 1
        count += 1
        amount -= denominations[coinIndex]
    print(count)


def getMinCoinChanges_improved(amount: int, coins: List[int]): # ------ time O(len(coins)) space O(1)
    denominations = deepcopy(coins)
    denominations.sort(reverse = True)
    count: int = 0
    index: int = 0
    while amount > 0:
        if denominations[index] > amount:
            index += 1
        else:
            count += 1
            amount -= denominations[index]

    print(count)




denominations = [1, 2, 5, 10, 20, 50, 1000, 100]
amount = 70

getMinCoinChanges(amount, denominations)
getMinCoinChanges_improved(amount, denominations)
# print(denominations)
# print(amount)