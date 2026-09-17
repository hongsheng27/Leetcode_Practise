class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        maxArea = 0

        for r in range(ROWS):
            dp[r][0] = int(matrix[r][0])
            maxArea = max(maxArea, dp[r][0] ** 2)
        for c in range(COLS):
            dp[0][c] = int(matrix[0][c])
            maxArea = max(maxArea, dp[0][c] ** 2)

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    maxArea = max(maxArea, dp[r][c] ** 2)
        return maxArea