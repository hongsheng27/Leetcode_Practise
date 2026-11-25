class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        isFirstRowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                       isFirstRowZero = True
                    else: 
                        matrix[r][0] = 0                    
                
        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLS):
                    matrix[r][c] = 0
        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(1, ROWS):
                matrix[r][0] = 0
        if isFirstRowZero:
            for c in range(COLS):
                matrix[0][c] = 0
                
        
