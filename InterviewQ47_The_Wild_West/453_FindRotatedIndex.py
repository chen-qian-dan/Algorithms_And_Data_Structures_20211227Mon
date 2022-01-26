"""
453 - Find Rotated Index

func findRotatedIndex accepts a rotated array of sorted numbers and an integer. 
The func should return the index of the integer in the array. 
If the value is not found, return -1

Time Complexity: O(log n)
Space Complexity: O(1)

findRotatedIndex([3, 4, 1, 2], 4) # 1
findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 8) # 3
findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3) # 6
findRotatedIndex([37, 44, 66, 102, 10, 22], 14) # -1
findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12) # -1
findRotatedIndex([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16) # 5

import math

def findRotatedIndex(arr, num):
"""


import math

def findRotatedIndexVideo(arr, num):
    left = 0
    right = len(arr) - 1
    if right>0 and arr[left] >= arr[right]:
        middle = math.floor((left + right) / 2)
        while (arr[middle] <= arr[middle + 1]):
            if arr[left] <= arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = math.floor((left + right) / 2)
            # if middle+1 > len(arr)-1: # for case ([4, 4], 4))
            #     break
        
 
        if (num >= arr[0] and num <= arr[middle]):
            left = 0
            right = middle
        else:
            left = middle + 1
            right = len(arr) - 1
    
    while (left <= right):
        middle = math.floor((left + right) / 2)
        if (num == arr[middle]):
            return middle
        if (num > arr[middle]):
            left = middle + 1
        else:
            right = middle - 1
    return -1


def findRotatedIndex(arr, num):
    # find the index of maxima 
    if len(arr) == 0:
        return -1
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] > arr[j] and i + 1 == j:
            break 
        mid = (i + j) // 2
        if arr[mid] < arr[0]:
            j = mid - 1
        else:
            i = mid + 1
    

    indexMaxima = i
    # search left
    i = 0
    j = indexMaxima
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == num:
            return mid 
        if arr[mid] < num:
            i = mid + 1
        else:
            j = mid - 1

    i = indexMaxima + 1
    j = len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == num:
            return mid 
        if arr[mid] < num:
            i = mid + 1
        else:
            j = mid - 1
    return -1 



# print(findRotatedIndex([3, 4, 1, 2], 4)) # 1
# # print(findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 8)) # 3
# # print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
# # print(findRotatedIndex([37, 44, 66, 102, 10, 22], 14)) # -1
# # print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
# # print(findRotatedIndex([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16)) # 5


# print(findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 1)) # 5

# print(findRotatedIndex([4, 4], 4)) # 

# print(findRotatedIndexVideo([4, 3], 2))
# print(findRotatedIndexVideo([4, 6, 7, 8, 9, 10, 1, 2, 3, 4], 1)) # 5

print(findRotatedIndexVideo([3, 4, 1, 2], 4)) # 1
print(findRotatedIndexVideo([4, 6, 7, 8, 9, 1, 2, 3, 4], 8)) # 3
print(findRotatedIndexVideo([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndexVideo([37, 44, 66, 102, 10, 22], 14)) # -1
print(findRotatedIndexVideo([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
print(findRotatedIndexVideo([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16)) # 5
print(findRotatedIndexVideo([4, 4], 4)) # 1