import numpy as np

arr = np.array([1, 2, 3], [4, 5, 6])
print(arr)



def insertOneRow(arr, newRow):
    newArr = np.insert(arr, 0, newRow, axis = 0) # 0 means row
    return newArr


print(insertOneRow(arr, [7, 8, 9]))


def insertOneColumn(arr, newColumn):
    newArr = np.insert(arr, 0, newColumn, axis = 1) 
    return newArr


newArr = np.append(arr, [[1, 2, 3]], axis = 0)


def access(arr, row: int, column: int):
    if row >= len(arr) or column >= len(arr[0]):
        print("Index out of range")
        return 
    return arr[row][column]


def traverse(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j])



def search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return (i, j) 
    return False 


def deleteARow(arr, rowIndex):
    newArr = np.delete(arr, rowIndex, axis = 0)

    return newArr


def deleteAColumn(arr, colIndex):
    newArr = np.delete(arr, colIndex, axis = 1)
    return newArr


