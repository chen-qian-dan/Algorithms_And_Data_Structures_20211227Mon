from typing import List

def binary_search(lst: List[int], val): # time O(logN), space O(1)
    if len(lst) == 0:
        raise ValueError("The list is empty")
    
    i = 0
    j = len(lst) - 1
    while i <= j:
        mid = (i + j) // 2
        if lst[mid] == val:
            return mid
        if lst[mid] < val:
            i = mid + 1
        else:
            j = mid - 1
    return False 


lst = [1, 2, 3, 4, 5]
print(binary_search(lst, 6))