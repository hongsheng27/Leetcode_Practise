class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        freshAmount = 0
        res = 0
        visit = set()
        queue = deque()
        def bfs(q):
            nonlocal freshAmount
            print(q)
            nei = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            count = -1
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in nei:
                        nr, nc = row + dr, col + dc
                        if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                            grid[nr][nc] == 0 or grid[nr][nc] == 2 or (nr, nc) in visit): 
                            continue
                        freshAmount -= 1
                        visit.add((nr, nc))
                        q.append((nr, nc))
                count += 1
            return count

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshAmount += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2 and (row, col) not in visit:
                    queue.append((row, col))
        res = max(res, bfs(queue))
        return -1 if freshAmount > 0 else res