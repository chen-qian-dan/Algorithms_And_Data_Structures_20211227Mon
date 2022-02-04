"""
Given an array of integer of size N, find maximum sum of K consequtive elements
"""

from typing import List 
def maxSum(lst: List[int], k: int) -> int:
    if len(lst) < k:
        raise ValueError(f"Length of input list muster equal or larger than {k}")
    if len(lst) == k:
        return sum(lst)
    
    maxSum = sum(lst[0:k])
    newSum = maxSum 
    for i in range(k, len(lst)):
        newSum = newSum + lst[i] - lst[i - k]
        maxSum = newSum if newSum > maxSum else maxSum 

    return maxSum

arr = [80, -50, 90, 100]
k = 2 
ret = maxSum(arr, k) # 190
print(ret)