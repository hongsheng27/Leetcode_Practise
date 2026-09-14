class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                left = dp[r][c - 1] if c - 1 >= 0 else float('inf')
                top = dp[r - 1][c] if r - 1 >= 0 else float('inf')
                minTotal = min(left, top)
                minTotal = 0 if minTotal == float('inf') else minTotal
                dp[r][c] = minTotal + grid[r][c]
        return dp[ROWS - 1][COLS - 1]

        