

# Sorting
from typing import List 
import math

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


def bucketSort(lst: List[int]):
    bucketCount = round(math.sqrt(len(lst)))
    maxValue = max(lst)
    buckets = list()
    for i in range(bucketCount):
        buckets.append(list())
    for i in lst:
        index = math.ceil(i * bucketCount / maxValue)
        buckets[index - 1].append(i)
    for l in buckets:
        insertionSort(l)

    retList = list()
    for b in buckets:
        retList.extend(b)
    return retList



def merge(lst: List[int], l: int, m: int, r: int):
    n1: int = m - l + 1
    n2: int = r - m

    L: List[int] = [0] * n1
    R: List[int] = [0] * n2

    for i in range(n1):
        L[i] = lst[l + i]

    for i in range(n2):
        R[i] = lst[m + i + 1] 

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        lst[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        lst[k] = L[j]
        j += 1
        k += 1



def mergeSort(lst: List[int], l: int, r: int):
    if l < r:
        m = (l + r ) // 2
        mergeSort(lst, l, m)
        mergeSort(lst, m + 1, r)
        merge(lst, l, m, r)


def partition(lst: List[int], low: int, high: int):
    pivot: int = lst[high]
    L: int = low
    R: int = high - 1
    while L < high:
        if lst[L] > pivot:
            while R > L and lst[R] > pivot:
                R -= 1

            if L == R:
                lst[L], lst[high] = lst[high], lst[L]
                return L
            else:
                lst[L], lst[R] = lst[R], lst[L]
        L += 1
    return high


def partition(lst: List[int], low: int, high: int):
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1





def quickSort(lst: List[int], low: int, high: int):
    if low < high:
        pi = partition(lst, low, high)
        quickSort(lst, low, pi - 1)
        quickSort(lst, pi + 1, high)

    
lst = [3, 5, 8, 1, 2, 9, 4, 7, 6]
# bubbleSort(lst)
# selectionSort(lst)
# insertionSort(lst)
# lst = bucketSort(lst)
# mergeSort(lst, 0, 4)
quickSort(lst, 0, len(lst)-1)
print(lst)


