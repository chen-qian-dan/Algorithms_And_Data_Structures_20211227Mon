

from typing import List

def linear_search(lst: List[int], val): # time O(N), space O(1)
    if len(lst) == 0:
        raise ValueError("The list is empty")
    for i, v in enumerate(lst):
        if val == v:
            return i
    return False 


lst = [1, 2, 3, 4, 5]
print(linear_search(lst, 59))