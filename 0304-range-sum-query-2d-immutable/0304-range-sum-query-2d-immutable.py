class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0])
        rows = len(matrix)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for n in range(1, rows + 1):
            for m in range(1, cols + 1):
                self.prefix[n][m] = matrix[n - 1][m - 1] + self.prefix[n][m - 1] +  self.prefix[n - 1][m] - self.prefix[n - 1][m - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)