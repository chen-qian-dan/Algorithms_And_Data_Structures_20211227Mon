"""
Divide and Conquer:
405 - Number of paths to reach the last cell with given cost

- Given 2D matrix
- Each cell has a cost associated with it for accessing
- We need to start from (0, 0) cell and go till (n-1, n-1) cell
- We can go only to right or down cell from current cell 
- We are given total cost to reach the last cell
- Find the number of ways to reach end of matrix with given "total cost"

1. Problem
Can the cost be negative? No
Can totalCost be negative? No
2. Input: matrix, totalCost
3. Output: int 
4. Edge cases:
5. Time complexity
6. Space complexity
"""

from typing import List 

def getPathsCountForward(matrix: List[List[int]], totalCost: int, r: int, c: int) -> int:
    if r >= len(matrix) or c >= len(matrix[0]):
        return 0
    if r == len(matrix) - 1 and c == len(matrix[0]) - 1:
        if totalCost == matrix[r][c]:
            return 1
        else:
            return 0

    if matrix[r][c] <= totalCost:
        a = getPathsCountForward(matrix, totalCost - matrix[r][c], r, c + 1)
        b = getPathsCountForward(matrix, totalCost - matrix[r][c], r + 1, c)
        return (a + b)
    
    return 0


def getPathsCountBackward(matrix: List[List[int]], totalCost: int, r: int, c: int) -> int:
    if totalCost < 0:
        return 0
    if r < 0 or c < 0:
        return 0
    if r == 0 and c == 0:
        if matrix[r][c] == totalCost:
            return 1
        else:
            return 0

    if matrix[r][c] <= totalCost:
        a = getPathsCountBackward(matrix, totalCost - matrix[r][c], r, c - 1)
        b = getPathsCountBackward(matrix, totalCost - matrix[r][c], r - 1, c)
        return (a + b)
    
    return 0


matrix = [[4, 7, 1, 6], 
            [5, 7, 3, 9], 
            [3, 2, 1, 2], 
            [7, 1, 6, 3]] # expect 2

totalCost = 25

print(getPathsCountForward(matrix, totalCost, 0, 0))
print(getPathsCountBackward(matrix, totalCost, 3, 3))