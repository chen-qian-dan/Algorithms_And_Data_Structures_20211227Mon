
"""
How to find the missing number in an integer array of 1 to 100?

Q: if this array is not in order, then use:
    sum(1, ..., 100) = (1 + 100) * 100 / 2 = 5500
Q: does that means the input list length is alway 99?
"""

from typing import List

def findMissingNumber(lst: List[int], nMin: int, nMax: int) -> int:
    nMissngNumber: int = int((nMin + nMax) * nMax / 2) - sum(lst)
    return nMissngNumber
