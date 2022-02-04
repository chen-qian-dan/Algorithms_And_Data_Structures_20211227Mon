"""
Write a function to find the missing number in a given integer array of 1 to 100. 
missingNumber([1, 2, 3, 4, 6], 6) # 5
"""

from typing import List 
def missingNumber(lst: List[int], n: int) -> int:
    sumExpected = (1 + n) * n / 2
    sumActual = sum(lst)
    return sumExpected - sumActual


lst = [1, 2, 3, 4, 6]
n = 6
ret = missingNumber(lst, n)
print(ret)