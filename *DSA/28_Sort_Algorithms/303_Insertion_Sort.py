

from typing import List
def insertion_sort(lst: List[int]): # by ref time O(n^2), space O(1)
    if len(lst) <= 1:
        pass
    else:
        for l in range(0, len(lst) - 1):
            for r in range(l + 1, 0, -1):
                if lst[r] < lst[r - 1]:
                    lst[r - 1], lst[r] = lst[r], lst[r - 1]
                else:
                    break 



lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
lst = [3]
insertion_sort(lst)

print(lst)