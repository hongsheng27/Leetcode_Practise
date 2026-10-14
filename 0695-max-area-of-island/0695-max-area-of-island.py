class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # dfs: can return value back to start
        # 1:25
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] != 1 or (r, c) in visited): return 0
            visited.add((r, c))
            return (
                1 + 
                dfs(r + 1, c) +
                dfs(r - 1, c) + 
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res