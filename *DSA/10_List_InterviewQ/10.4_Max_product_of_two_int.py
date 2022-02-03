"""
Find max product of two integers in the list where all items are positive

1. problem
2. intput
3. output
4. edge case
5. time
6. space
"""


lst = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21] # 57 * 58 = 3306

from typing import List 
def findMaxProductOfTwo(lst: List[int]) -> int:
    if len(lst) < 2:
        raise ValueError("len(lst) >= 2 must be True")
    first = 0
    second = 0
    for v in lst:
        if v >= first:
            second = first
            first = v
        elif v > second:
            second = v
    return first * second 


print(findMaxProductOfTwo(lst))

