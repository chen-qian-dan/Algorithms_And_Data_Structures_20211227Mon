
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


lst: List[int] = [1, 20, 3, 4, 11, 5]


print(findMaxProductOfTwo(lst))

    