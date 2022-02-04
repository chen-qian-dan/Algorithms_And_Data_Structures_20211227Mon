"""
The array must be sorted
"""

from typing import List, Optional, Union 
def binarySearch(lst: List[int], target: int) -> Optional[Union[bool, int]]:
    if lst is None:
        raise ValueError("List can not be None")
    if len(lst) == 0:
        return None 
    i = 0
    j = len(lst) - 1
   
    while i <= j:
        middle = (i + j) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            i = middle + 1
        else:
            j = middle - 1

    return False


arr = [1, 2, 3, 4, 5, 6]
target = 6

ret = binarySearch(arr, target)
print(ret)
