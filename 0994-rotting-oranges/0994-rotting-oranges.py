class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        q = deque()
        freshAmount = res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    freshAmount += 1
        while q and freshAmount > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                        (nr, nc) in visited or grid[nr][nc] != 1): continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    freshAmount -= 1
            res += 1 
        return -1 if freshAmount > 0 else res


