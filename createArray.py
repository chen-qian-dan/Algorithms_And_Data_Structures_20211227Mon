from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1, 2, 3])

print(arr1)
print(arr2)

"""
output:
array('i', [1, 2, 3, 4, 5, 6])
array('d', [1.0, 2.0, 3.0])
"""




# # insertion
# arr1.insert(len(arr1) - 1, 9) # when array is full, insertion will create a larger array
# print(arr1)
# """
# output:
# array('i', [1, 2, 3, 4, 5, 9, 6])
# """


# traversal (loop)
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)
