class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visited or grid[r][c] == "0"):
                return 0
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return 1
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res += dfs(row, col)
        return res
        
