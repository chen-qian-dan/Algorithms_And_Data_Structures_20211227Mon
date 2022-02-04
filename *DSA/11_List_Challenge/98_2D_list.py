"""
Given 2D list calculate the sum of diagonal elements

myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumDiagonal(myList2D) # 15

"""
from typing import List 
def sumDiagonal(lst: List[List[int]]) -> int:
    if lst is None:
        raise ValueError("Input can not be None")
    m = len(lst)
    n = len(lst[0])
    if m != n:
        raise ValueError("The input must be a rectangle matrix")
    sum = 0
    for i in range(m):
        sum += lst[i][i]
    return sum


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ret = sumDiagonal(myList2D) # 15
print(ret)
