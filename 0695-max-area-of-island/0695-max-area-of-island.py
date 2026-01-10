class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            count = 1
            while q:
                row, col = q.popleft()
                for dr, dc in neighbors:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 0: continue
                    visit.add((r, c))
                    count += 1
                    q.append((r, c))
            return count

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visit:
                    res = max(res, bfs(i, j))
        return res
        