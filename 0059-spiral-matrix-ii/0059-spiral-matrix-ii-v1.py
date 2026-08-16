class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[-1] * n for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        row, col = 0, 0
        num = 0
        start = False
        while top <= bottom and left <= right:
            if row == top and col == left and not start:
                start = True
            elif row == top and col == left and start:
                top += 1
                right -= 1
                bottom -= 1
                left += 1
                row += 1
                col += 1
                start = False
                continue
            num += 1
            grid[row][col] = num
            if row == top and col < right:
               col += 1 
            elif col == right and row < bottom:
                row += 1
            elif row == bottom and left < col:
                col -= 1
            elif col == left and top < row:
                row -= 1
        return grid