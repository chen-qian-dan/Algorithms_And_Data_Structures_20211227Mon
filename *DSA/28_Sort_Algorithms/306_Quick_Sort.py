
from typing import List 

def quick_sort(lst: List[int], l: int, h: int):
    if l < h:
        pivot = lst[h]
        i = l - 1
        for j in range(l, h):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[h] = lst[h], lst[i + 1]
        quick_sort(lst, l, i)
        quick_sort(lst, i + 2, h)

lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
# lst = [3]
quick_sort(lst, 0, len(lst) - 1)

print(lst)