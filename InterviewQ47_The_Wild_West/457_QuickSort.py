

"""
47_The Wild West: 457_Quick Sort
def pivot (arr, comparator=None, start=0):
    # TODO

def quickSort(arr, comparator=None, start = 0, end=0):
    # TODO
"""



def pivot (arr, comparator=None, start=0):
    # TODO
    if callable(comparator) == False:
        def comparator(a, b):
            if a < b:
                return -1
            if a > b:
                return 1
            return 0
    i = start
    for j in range(start + 1, len(arr)):
        if comparator(arr[j], arr[start]) < 0:  # note: can not be <= 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[start] = arr[start], arr[i]
    return i 


def quickSort(arr, comparator=None, start = 0, end=0):
    # TODO
    if start < end:
        pivotIndex = pivot(arr, comparator, start)
        quickSort(arr, comparator, start, pivotIndex - 1)
        quickSort(arr, comparator, pivotIndex + 1, end)
    return arr 



# def pivot (arr, comparator=None, start=0):
#     if callable(comparator)==False:
#         def comparator(a,b):
#             if a < b:
#                 return -1
#             if a > b:
#                 return 1
#             return 0
#     pivotIndex = start
#     for i in range(start+1,len(arr)):
#         if comparator(arr[start], arr[i]) > 0:
#             pivotIndex += 1
#             [arr[i], arr[pivotIndex]] = [arr[pivotIndex], arr[i]]
#     if pivotIndex != start:
#         [arr[pivotIndex], arr[start]] = [arr[start], arr[pivotIndex]]
    
#     return pivotIndex
 
# def quickSort(arr, comparator=None, start = 0, end=0):
#     if start < end:
#         pivotIndex = pivot(arr, comparator, start)
#         quickSort(arr, comparator, start, pivotIndex - 1)
#         quickSort(arr, comparator, pivotIndex + 1, end)
#     return arr


arr = [5, 4, 9, 10, 2, 20, 8, 7, 3, 5]
print(quickSort(arr, start = 0, end = len(arr) - 1))

arr = [8, 4, 2, 5, 0, 10, 11, 12, 13, 16]
print(quickSort(arr, start = 0, end = len(arr) - 1))