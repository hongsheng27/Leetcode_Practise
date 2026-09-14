class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = grid[0][0]

        for r in range(1, ROWS):
            dp[r][0] = dp[r - 1][0] + grid[r][0]
        for c in range(1, COLS):
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = min(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]
        return dp[ROWS - 1][COLS - 1]

        