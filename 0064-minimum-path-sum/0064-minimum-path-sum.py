class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
  
        def dfs(r, c, cache):
            if r == ROWS or c == COLS: return float('inf')
            if (r, c) in cache: return cache[(r, c)]
            if r == ROWS - 1 and c == COLS - 1: return grid[ROWS - 1][COLS - 1]
            
            cache[(r, c)] = grid[r][c] + min(dfs(r + 1, c, cache), dfs(r, c + 1, cache))
            return cache[(r, c)]
        return dfs(0, 0, {})

        