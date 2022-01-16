

# Sorting
from typing import List 

def bubbleSort(lst: List[int]): # by ref
    for j in range(len(lst) - 1, 0, -1):
        for i in range(0, j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def selectionSort(lst: List[int]):
    for i in range(len(lst)):
        minIndex = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]


def insertionSort(lst: List[int]):
    for i in range(len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

lst = [5, 4, 3, 2, 1] 
# bubbleSort(lst)
# selectionSort(lst)
insertionSort(lst)
print(lst)


