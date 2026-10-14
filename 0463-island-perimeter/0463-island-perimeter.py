class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # bfs / dfs
        # perimeter: if meet border res += 1
        # 10:00
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0: return 1
            if (r, c) in visited: return 0
            visited.add((r, c))
            return (dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r, c + 1) +
                    dfs(r, c - 1))
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    print(res)
                    res += dfs(r, c)
                    print(res)
        return res
        