class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # bfs find shortest path, only zero can pass
        # eight way to traverse
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1] == 1: return -1
        q = deque([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1), (1, 1), (-1, 1)]
        visited = {(0, 0)}
        minutes = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == (ROWS - 1, COLS - 1): return minutes + 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visited or grid[nr][nc] != 0): continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
            minutes += 1
        return -1


        