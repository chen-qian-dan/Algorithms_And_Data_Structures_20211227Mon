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

def HouseRobber(houses: List[int]) -> int:
    """
    for the 1st house, only have two options, 
    either steal or no
    """
    if len(houses) == 0:
        return 0
    elif len(houses) == 1:
        return houses[0]
    elif len(houses) == 2:
        return max(houses)

    firstH = houses[0] + HouseRobber(houses[2:])
    notFirstH = HouseRobber(houses[1:])

    return max(firstH, notFirstH)


houses = [6, 7, 1, 30, 8, 2, 4]
print(HouseRobber(houses))


def HouseRobberVideo(houses: List[int], houseIndex: int) -> int:
    if houseIndex >= len(houses):
        return 0 

    firstH = houses[houseIndex] + HouseRobberVideo(houses, houseIndex + 2)
    notFirstH = HouseRobberVideo(houses, houseIndex + 1)
    return max(firstH, notFirstH)

print(HouseRobberVideo(houses, 0))

