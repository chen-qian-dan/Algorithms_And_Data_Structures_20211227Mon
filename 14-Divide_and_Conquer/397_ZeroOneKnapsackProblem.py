"""
Divide and conquer:
397- Zero One Knapsack
- Given the weights and profits of N items
- Find the maximum profit within given capacity of C
- Items cannot be broken 

1. Problem:
    Can not get the same item twice except there are two such item in the list 
2. Input: [(weight = 4, profit = 5), (), ...]
3. Output: int
4. edge cases
C = 0, any item with zero weight
5. time complexity
6. space complextiy 

"""

from typing import List, Tuple

def zeroOneKnapsack(lst: List[Tuple[int, int]], C: int, index: int) -> int:

    if C <= 0:
        return 0
    if index >= len(lst) or index < 0:
        return 0

    if lst[index][0] <= C:
        pick = lst[index][1] + zeroOneKnapsack(lst, C - lst[index][0], index + 1)
        skip = zeroOneKnapsack(lst, C, index + 1)
        return max(pick, skip)
    else:
        return zeroOneKnapsack(lst, C, index + 1) # it is correct if return 0


lst = [(3, 31), (1, 26), (2, 17), (5, 72)]
C = 7


print(zeroOneKnapsack(lst, C, 0))