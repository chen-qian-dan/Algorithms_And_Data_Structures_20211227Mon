
# Find max product of two integers in the list where all items are positive
from typing import List


def findMaxProductOfTwo(lst: List[int]) -> int:
    if len(lst) == 2:
        return sum(lst)
    nMin: int = min(lst[0], lst[1])
    nMax: int = max(lst[0], lst[1])

    for v in lst[2:]:
        if v >= nMax:
            nMin = nMax
            nMax = v
        elif v > nMin:
            nMin = v
    return nMin * nMax


lst: List[int] = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21] # 57 * 58 = 3306


print(findMaxProductOfTwo(lst))

    