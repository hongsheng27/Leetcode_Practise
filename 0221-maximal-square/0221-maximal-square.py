class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range((ROWS + 1))]
        maxSide = 0

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    maxSide = max(maxSide, dp[r][c])
        return maxSide ** 2