class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in visit: 
                return 
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in visit:
                    dfs(i, j)
                    count += 1
        return count

        