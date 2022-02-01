"""
Given an array of integers of size N, 
find maximum sum of K consequtive elements. 
"""

from typing import List 

def slideWindowSum(lst: List[int], k: int) -> int:
    if len(lst) == 0:
        return 0
    if k > len(lst):
        raise ValueError(f"K: {k} must >= len(lst): {len(lst)}")

    maxSum: int = sum(lst[:k])
    for i in range(k, len(lst)):
        sum = maxSum + lst[i] - lst[i - k + 1]
        maxSum = max(sum, maxSum)

    return maxSum 


lst = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2
print(slideWindowSum(lst, k))