"""
Divide and Conquer

House Robber
- Given N number of houses along the street with some amount of money
- Adjacent houses cannot be stolen
- Find the maximum amount that can be stolen

1. problem
2. input: houses = [3, 5, 1, 9]
3. output: maxAmount >= 0
4. edge case: 
    houses = [], maxAmount = 0
    houses = [1], maxAmount = 1
    houses = [1, 2], maxAmount = 2
5. time complexity
6. space complexity 
"""

from typing import List
def house_robber(houses: List[int]) -> int:
    if len(houses) == 0:
        return 0
    sub1 = houses[0] + house_robber(houses[2:])
    sub2 = house_robber(houses[1:])
    return max(sub1, sub2)


houses = [6, 7, 1, 30, 8, 2, 4] # expect 41
print(house_robber(houses))