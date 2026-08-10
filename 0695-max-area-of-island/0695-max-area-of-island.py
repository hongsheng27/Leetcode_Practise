class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxTotal = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r, c))
            return (1 + 
                    dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))
        for row in range(ROWS):
            for col in range(COLS):
                total = dfs(row, col)
                maxTotal = max(total, maxTotal)
        return maxTotal