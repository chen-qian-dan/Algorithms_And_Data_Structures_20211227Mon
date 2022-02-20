
from typing import List 

def selection_sort(lst: List[int]): # by ref 
    if len(lst) <= 1:
        pass 
    else:
        for l in range(0, len(lst)):
            minIndex = l
            for r in range(l, len(lst)):
                if lst[r] < lst[minIndex]:
                    minIndex = r
            lst[l], lst[minIndex] = lst[minIndex], lst[l]



lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
lst = [3]
selection_sort(lst)

print(lst)
