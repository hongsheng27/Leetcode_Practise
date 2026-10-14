class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs / bfs, traverse and claim visited
        # only if I don't visit can start dfs, if start dfs, res += 1
        # 2:30
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visited: return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        return res
