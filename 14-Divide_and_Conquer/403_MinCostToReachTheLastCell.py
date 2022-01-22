"""
Divide and Conquer:
403 - Minimum cost to reach the last cell

- 2D matrix is given 
- Each cell has a cost associated with it for accessing
- We need to start from (0, 0) cell and go till (n-1, n-1) cell
- We can go only to right or down cell from current cell
- Find the way in which the cost is minimum 

1. Problem
2. Input: 2D list
3. Output: int
4. Edge case 
5. Time complexity
6. Space complexity 
"""

from typing import List 
import math 

def getMinCostBackward(matrix: List[List[int]], r: int, c: int) -> int:

    if r <= -1 or c <= -1:
        return math.inf
    if r == 0 and c == 0:
        return matrix[r][c]

    a = matrix[r][c] + getMinCostBackward(matrix, r - 1, c)
    b = matrix[r][c] + getMinCostBackward(matrix, r, c - 1)

    return min(a, b)



def getMinCostForward(matrix: List[List[int]], r: int, c: int) -> int:
    if r >= len(matrix) or c >= len(matrix[0]):
        return math.inf
    if r == len(matrix) - 1 and c == len(matrix[0]) - 1:
        return matrix[r][c]

    a = matrix[r][c] + getMinCostForward(matrix, r, c + 1)
    b = matrix[r][c] + getMinCostForward(matrix, r + 1, c)
    return min(a, b)


matrix = [[4, 7, 8, 6, 4], 
            [6, 7, 3, 9, 2], 
            [3, 8, 1, 2, 4], 
            [7, 1, 7, 3, 7], 
            [2, 9, 8, 9, 3]] # expect 36

print(getMinCostBackward(matrix, 4, 4))
print(getMinCostForward(matrix, 0, 0))

