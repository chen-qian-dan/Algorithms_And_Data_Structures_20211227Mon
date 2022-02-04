"""
Given a list, write a function to get first, second best scores from the list. 
List may contain duplicates. 

myList = [84, 85, 86, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
firstSecond(myList) # 90, 87
"""
from typing import List, Tuple
def firstSecond(lst: List[int]) -> Tuple[int, int]:
    if lst is None:
        raise ValueError("The input list can not be None")
    if len(lst) < 2:
        raise ValueError("len(lst) >= 2 must be True")

    first = 0
    second = 0 
    for v in lst:
        if v >= first:
            second = first
            first = v 
        elif v > second:
            second = v
    return (first, second)

myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
ret = firstSecond(myList) # 90, 87
print(ret)
