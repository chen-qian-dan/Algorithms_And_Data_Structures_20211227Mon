"""
How to check if an array contains a number in Python
"""
import numpy as np
arr = np.array([1, 20, 3, 4, 5, 7])

def findNumber(arr, target) -> bool:

    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False 
