class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in neighbors:
                    r,c  = row + dr, col + dc
                    if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == "0":
                        continue
                    q.append((r, c))
                    visit.add((r, c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    count += 1
        return count


        
        