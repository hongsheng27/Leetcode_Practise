class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.newMatrix = []
        for mat in matrix:
            sum = 0
            prefixRow = [0]
            for m in mat:
                sum += m
                prefixRow.append(sum)
            self.newMatrix.append(prefixRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += (self.newMatrix[r][col2 + 1] - self.newMatrix[r][col1])
        return res
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)