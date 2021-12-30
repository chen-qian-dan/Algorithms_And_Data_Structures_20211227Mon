import numpy as np

# create two dimentional array
twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDArray)


# insertion
# can not insert one element
# can insert one column
# can insert one row

newTwoDArray = np.insert(twoDArray, 0, [10, 11, 12], axis= 1) # 0: row, 1: column
print(newTwoDArray)

newTwoDArray = np.insert(twoDArray, 0, [10, 11, 12], axis= 0) # 0: row, 1: column
print(newTwoDArray)
