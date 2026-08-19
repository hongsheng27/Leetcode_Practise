class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(starts):
            q = deque(starts)
            visit = set(starts)
            while q:
                row, col = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS
                        or (nr, nc) in visit or heights[nr][nc] < heights[row][col]): continue
                    visit.add((nr, nc))
                    q.append((nr, nc))
            return visit

        pacific = []
        atlantic = []
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic.append((r, c))
        
        return list(bfs(pacific) & bfs(atlantic))