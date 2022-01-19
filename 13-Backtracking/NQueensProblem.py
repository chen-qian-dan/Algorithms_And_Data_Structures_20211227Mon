# N Queens Problem

from typing import List, Tuple 

def isSave(queensLocations: List[Tuple[int, int]], location: Tuple[int, int], N: int) -> bool:
    diagonals: List[Tuple[int, int]] = list()
    row: int = location[0]
    column: int = location[1]
    if row - 1 >= 0 and column - 1 >= 0:
        diagonals.append((row - 1, column - 1))
    if row - 1 >= 0 and column + 1 < N:
        diagonals.append((row - 1, column + 1))

    if row + 1 < N and column + 1 < N:
        diagonals.append((row + 1, column + 1))
    if row + 1 < N and column - 1 >= 0:
        diagonals.append((row + 1, column - 1))
    
    for v in queensLocations:
        if v[0] == location[0] or v[1] == location[1] or v in diagonals:
            return False 
    return True 


def placeNQueens(N: int, queensLocations: List[Tuple[int, int]]):
    """
    print result
    """
    if len(queensLocations) == N:
        print(queensLocations)
        return True 

    for r in range(N):
        for c in range(N):
            if isSave(queensLocations, (r, c), N):
                queensLocations.append((r, c))
                if placeNQueens(N, queensLocations):
                    return True
                else: 
                    queensLocations.pop(0)
                    placeNQueens(N, queensLocations)
            else:
                queensLocations.pop(0)
                placeNQueens(N, queensLocations)


    return False 



# placeNQueens(4, [])


class NQeens:
    def __init__(self, n):
        self.n = n 
        # be really careful about making 2D arrays
        # [[0]*n]*n will use '[0]*n' n times, which make all rows are the same
        self.chessTable = [[0] * n for i in range(n)] 

    def printTable(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.chessTable[r][c] == 1:
                    print(" Q ", end = "")
                else:
                    print(" - ", end = "")

            print("\n")

    def isPlaceSave(self, r: int, c: int) -> bool:
        for i in range(self.n):
            if self.chessTable[r][i] == 1:
                return False 
        j = c
        for i in range(r, -1, -1):
            if i < 0:
                break 
            if self.chessTable[i][j] == 1:
                return False 
            j -= 1
                
        j = c
        for i in range(r, self.n):
            if i < 0:
                break 
            if self.chessTable[i][j] == 1:
                return False 
            j -= 1

        return True 

    def solve(self, c: int):
        if c == self.n:
            return True 
        for r in range(self.n):
            if self.isPlaceSave(r, c):
                self.chessTable[r][c] = 1
                if self.solve(c + 1):
                    return True 
                self.chessTable[r][c] = 0
        return False 


    def SolveQ(self):
        if self.solve(0):
            self.printTable()
        else:
            print("There is no solution")
            


queens = NQeens(4)
# queens.printTable()
# queens.solve(0)
# queens.printTable()
queens.SolveQ()
        



    
        


