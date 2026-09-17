class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        maxSide = 0

        for r in range(ROWS):
            dp[r][0] = int(matrix[r][0])
            maxSide = max(maxSide, dp[r][0])
        for c in range(COLS):
            dp[0][c] = int(matrix[0][c])
            maxSide = max(maxSide, dp[0][c])

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    maxSide = max(maxSide, dp[r][c])
        return maxSide ** 2