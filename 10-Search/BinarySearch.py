# Binary search

def binarySearch(lst, value) -> int:
    """
    return index if found else -1
    """
    i: int = 0
    j: int = len(lst) - 1
    while i <= j:
        mid: int = (i + j) // 2   
        if lst[mid] == value:
            return mid
        else:
            if value < lst[mid]:
                j = mid - 1
            else:
                i = mid + 1 
    return -1


def recursiveBinarySearch(lst, value, i: int, j: int) -> int:
    """
    return index if found else -1
    """
    if i > j:
        return -1
    mid: int = (i + j) // 2
    if lst[mid] == value:
        return mid 
    else:
        if lst[mid] < value:
            return recursiveBinarySearch(lst, value, mid + 1, j)
        else:
            return recursiveBinarySearch(lst, value, i, mid - 1)



    
lst = [1, 2, 3, 4, 5, 6]
# print(binarySearch(lst, 4))
print(recursiveBinarySearch(lst, 1, 0, len(lst) - 1))