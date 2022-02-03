"""
Find a number in an array
1. problem: sorted ?
2. input, what type
3. output
4. edge case
5. time complexity
6. space 
"""


import numpy as np
arr = np.array([1, 2, 3, 4])

def findANumber(arr, target):
    # linear search
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return "The number is not in the array"