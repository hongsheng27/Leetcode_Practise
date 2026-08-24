class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = left = 0
        bottom = right = n - 1
        board = [[0] * n for _ in range(n)]
        start = 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
               board[top][col] = start
               start += 1
            top += 1
            for row in range(top, bottom + 1):
                board[row][right] = start
                start += 1
            right -= 1
            for col in range(right, left - 1, -1):
                board[bottom][col] = start
                start += 1
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                board[row][left] = start
                start += 1
            left += 1
        return board
