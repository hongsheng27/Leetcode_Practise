class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS - 1][COLS - 1] == 1: return 0
        dp = [[0] * (COLS) for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if dp[r][c] == 1: continue
                if obstacleGrid[r][c] == 0:
                    bottom = 0 if r + 1 >= ROWS else dp[r + 1][c]
                    right = 0 if c + 1 >= COLS else dp[r][c + 1]
                    dp[r][c] = right + bottom
        return dp[0][0]