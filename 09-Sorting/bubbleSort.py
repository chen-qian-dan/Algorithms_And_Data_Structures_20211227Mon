

# Bubble sort
from typing import List 

def bubbleSort(lst: List[int]): # by ref
    for j in range(len(lst) - 1, 0, -1):
        for i in range(0, j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                


lst = [5, 4, 3, 2, 1] 
bubbleSort(lst)
print(lst)


