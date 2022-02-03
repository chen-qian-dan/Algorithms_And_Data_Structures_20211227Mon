"""
How to find the missing number in an integer array of 1 to 100?

Q: if this array is not in order, then use:
    sum(1, ..., 100) = (1 + 100) * 100 / 2 = 5500
Q: does that means the input list length is alway 99?

1. problem: only misse one, or multi
2. intput
3. output
4. edge case
5. time complexity 
6. space complexity
"""

from typing import List 
def findMissing(lst: List[int], n: int) -> int:
    sumExpected = (1 + n) * n / 2
    sumActrual = sum(lst)
    return sumExpected - sumActrual