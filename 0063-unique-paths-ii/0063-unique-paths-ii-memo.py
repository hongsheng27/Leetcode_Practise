class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # solution 1: dfs, the answer want distinct route, so I need every distinct route, but I forget the complicity, but 1 <= m, n <= 100 sound not too much
        # but TLE, try solution2: DP with memo
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS - 1][COLS - 1] == 1: return 0
        res = 0
        memo = {}
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                obstacleGrid[r][c] == 1):
                return 0
            if (r, c) in memo: return memo[(r, c)]
            if r == ROWS - 1 and c == COLS - 1: 
                return 1
            
            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]
            
        return dfs(0, 0)