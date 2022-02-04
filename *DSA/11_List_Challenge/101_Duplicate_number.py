"""
Write a function to find the duplicate number on given integer array/list. 

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
output: [1, 2, 3, 4, 5]
"""

from typing import List 
def removeDuplicates(lst: List[int]) -> List[int]:
    if lst is None:
        raise ValueError("The list can not be None")
    return list(set(lst))