class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshAmount = 0
        visit = set()
        q = deque()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minute = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    freshAmount += 1
        while q and freshAmount:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or
                        nc == COLS or grid[nr][nc] == 0 or
                        (nr, nc) in visit): continue
                    visit.add((nr, nc))
                    q.append((nr, nc))
                    freshAmount -= 1
            minute += 1
        
        return minute if not freshAmount else -1
        