

class NQueens:
    def __init__(self, n):
        self.n = n 
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def print_table(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end = "")
                else:
                    print(" - ", end = "")
            print("\n")

    def is_place_safe(self, r, c) -> bool:
        # only need to check left side

        for j in range(self.n):
            if self.chess_table[r][j] == 1:
                return False 

        # check point to top left
        i = r
        j = c
        while i >= 0 and j >= 0:
            if self.chess_table[i][j] == 1:
                return False 
            else:
                i -= 1
                j -= 1
        i = r
        j = c
        # check point to bottom left
        while i < self.n and j >= 0:
            if self.chess_table[i][j] == 1:
                return False 
            else:
                i += 1
                j -= 1
        return True 

    def solve(self, c):
        # if n = 4, the place is 0, 1, 2, 3
        # so, if c = 4, means all Q are placed
        if c == self.n:
            return True 

        for r in range(self.n):
            if self.is_place_safe(r, c):
                self.chess_table[r][c] = 1
                if self.solve(c + 1):
                    return True
                self.chess_table[r][c] = 0
        return False 

    def solve_NQueens(self):
        if self.solve(0):
            self.print_table()
        else:
            print("There is no solution") 
            


queens = NQueens(4)
# queens.print_table()
queens.solve_NQueens()

