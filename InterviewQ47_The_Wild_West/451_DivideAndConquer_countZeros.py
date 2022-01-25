"""
451 - Divide and Conquer - countZeroes
Given an array of 1s and 0s which has all 1s first followed by all 0s, 
write a func called countZeroes, which returns the number of zeros in the array. 

countZeroes([1, 1, 1, 1, 0, 0]) # 2
countZeroes([1, 0, 0, 0, 0]) # 4
countZeroes([0, 0, 0]) # 3
countZeroes([1, 1, 1, 1]) # 0

Time Complexity - O(logn)

# Divide and Conquer - countZeroes

def countZeroes(customList):
    # TODO

"""

# Divide and Conquer - countZeroes

def countZeroes(customList):
    # TODO
    if len(customList) == 0:
        return 0 
    if customList[0] == 1 and customList[-1] == 1:
        return 0
    if customList[0] == 0 and customList[-1] == 0:
        return len(customList)

    i = 0
    j = len(customList) - 1
    while i + 1 != j:
        middle = (i + j) // 2
        if customList[middle] == 1:
            i = middle
        else:
            j = middle
    return len(customList) - i - 1