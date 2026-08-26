class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque()
        landAmount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    landAmount += 1
                if (r in (0, ROWS - 1) or c in (0, COLS - 1)) and grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 2
                    landAmount -= 1
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or
                    grid[nr][nc] != 1): continue
                grid[nr][nc] = 2
                q.append((nr, nc))
                landAmount -= 1
        return landAmount

                