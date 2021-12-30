import numpy as np

# create two dimentional array
twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDArray)


# # insertion
# # can not insert one element
# # can insert one column
# # can insert one row

# newTwoDArray = np.insert(twoDArray, 0, [10, 11, 12], axis= 1) # 0: row, 1: column
# print(newTwoDArray)

# newTwoDArray = np.insert(twoDArray, 0, [10, 11, 12], axis= 0) # 0: row, 1: column
# print(newTwoDArray)


# append
newTwoDArray = np.append(twoDArray, [[1, 2, 3]], axis= 0)
print(newTwoDArray)


# access
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

def accessElements(array, rowIndex, columnIndex):
    if rowIndex < 0 or rowIndex > len(array) - 1 or columnIndex < 0 or columnIndex > len(array[0]) - 1:
        print('Incorrect index')

    else:
        print(array[rowIndex][columnIndex])

accessElements(twoDArray, 0, 0)



# traverse
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

for i in range(len(twoDArray)):
    for j in range(len(twoDArray[0])):
        print(twoDArray[i][j])


# search
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

def searchTwoDArray(twoDArray, target):

    for i in range(len(twoDArray)):
        for j in range(len(twoDArray[0])):
            if twoDArray[i][j] == target:
                return True
    return False


print(searchTwoDArray(twoDArray, 3))