class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [inf] * COLS
        dp[0] = 0
        for r in range(ROWS):
            for c in range(COLS):
                from_top = dp[c]
                from_left = dp[c - 1] if c - 1 >= 0 else float('inf')
                dp[c] = min(from_top, from_left) + grid[r][c]
        return dp[-1]