from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1, 2, 3])

print(arr1)
# print(arr2)

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


# # traversal (loop)
# def traverseArray(array):
#     for i in array:
#         print(i)

# traverseArray(arr1)



# # access
# def accessElement(array, index):
#     if index < 0 or index > len(array) - 1:
#         print(f"index {index} is out of range")
#     else:
#         print(array[index]) 

# accessElement(arr1, 100)


# # search
# def searchInArray(array, target):
#     for i, v in enumerate(array):
#         if v == target:
#             return i
#     return "The target does not exist"

# print(searchInArray(arr1, 6))


# delete
arr1.remove(6) # shit to LHS
print(arr1)
arr1.remove('not exist') # ValueError