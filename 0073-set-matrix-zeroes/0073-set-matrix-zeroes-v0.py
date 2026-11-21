class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowSet = set()
        colSet = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        for r in range(ROWS):
            for c in range(COLS):
                if r in rowSet or c in colSet:
                    matrix[r][c] = 0
        

        
            
            
                    

        