class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}

        def dfs(r, c):
            if (
                r >= ROWS or
                c >= COLS or
                obstacleGrid[r][c] == 1
            ):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = (
                dfs(r + 1, c)
                + dfs(r, c + 1)
            )

            return memo[(r, c)]

        return dfs(0, 0)