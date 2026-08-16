class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        num = 0
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                num += 1
                grid[top][col] = num
            top += 1
            for row in range(top, bottom + 1):
                num += 1
                grid[row][right] = num
            right -= 1
            for col in range(right, left - 1, -1):
                num += 1
                grid[bottom][col] = num
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                num += 1
                grid[row][left] = num
            left += 1
        return grid