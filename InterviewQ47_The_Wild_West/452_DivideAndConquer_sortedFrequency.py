"""
452 - Divide and Conquer - sortedFrequency
Given a sorted array and a number, write a function called sortedFrequency that counts the 
occurrences of the number in the array

sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2) # 4
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 3) # 1
sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4) # -1
sortedFrequency([], 4) # -1

Time Complexity - O(logN)

# Divide and Conquer - sortedFrequency
import math

def sortedFrequency(arr, num):
    # TODO

"""

# Divide and Conquer - sortedFrequency
import math

def sortedFrequency(arr, num):
    # TODO
    if len(arr) == 0:
        return -1
    if num < arr[0]:
        return -1
    if num > arr[-1]:
        return -1
    if arr[0] == num and arr[-1] == num:
        return len(arr)
    i = 0
    j = len(arr) - 1

    while i < j:
        mid = (i + j) // 2
        if num <= arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
            
    left = j if arr[j] == num else j + 1

    i = 0
    j = len(arr) - 1

    while i < j:
        mid = (i + j) // 2
        if num < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1

    right = i if arr[i] == num else i - 1
    return right - left + 1


print(sortedFrequency([1, 2, 3, 4, 5, 6, 7], 4)) # 1
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2)) # 4
print(sortedFrequency([1, 1, 2, 2, 2, 3, 4], 3)) # 1
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4)) # -1
print(sortedFrequency([], 4)) # -1