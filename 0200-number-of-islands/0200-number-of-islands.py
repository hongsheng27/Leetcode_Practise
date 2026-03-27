class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set() # (col, row)
        count = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visit or grid[r][c] == "0"): return
            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
       
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1
        return count

        