"""
Bubble sort / Sinking sort 
"""
from typing import List 

def bubble_sort(lst: List[int]): # by ref
    if len(lst) <= 1:
        pass 
    for j in range(len(lst) - 1, -1, -1):
        for i in range(0, j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
lst = [3]
bubble_sort(lst)

print(lst)
        
