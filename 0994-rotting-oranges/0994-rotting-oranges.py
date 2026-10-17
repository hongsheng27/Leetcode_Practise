class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # put every (r, c) = 2 into queue
        # muti bfs, add visited, every 1 rotten, amount -= 1, record every round after end of for _ in range(q)
        # if amount != 0 return -1, or return round
        # 03:15
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        freshAmount = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshAmount += 1
        minute = 0
        while q and freshAmount:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshAmount -= 1
                        q.append((nr, nc))
            minute += 1
        return -1 if freshAmount > 0 else minute

