from array import * 

arr1 = array('i', [1, 2, 3, 4, 5, 6])

if False:
    arr1.insert(7, 7)
    print(arr1)

    arr1.insert(17, 8) # insert after tail = insert at the tail
    print(arr1)


def traverseArray(arr):
    for i in arr:
        print(i)


def accessArray(arr, index: int):
    return arr[index]


def searchArray(arr, value) -> bool:
    for v in arr:
        if v == value:
            return True
    return False


def remove(arr, value):
    """
    - arr is by ref
    - if there are multi values, will remove the left one
    - ValueError if value is not in arr
    """
    arr.remove(value = value) # return None 


arr = [1, 2, 3, 4, 4, 5]
# traverseArray(arr1)
remove(arr, 4)
print(arr)
