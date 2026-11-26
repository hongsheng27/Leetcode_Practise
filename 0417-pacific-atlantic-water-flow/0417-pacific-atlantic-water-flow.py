class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        def bfs(start):
            q = deque(start)
            visited = set(start)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visited or heights[nr][nc] < heights[r][c]): continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
            
                
            return visited
        pacificStart = []
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacificStart.append((r, c))
        atlanticStart = []
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1:
                    atlanticStart.append((r, c))
        pacificSet = bfs(pacificStart)
        atlanticSet = bfs(atlanticStart)
        return [[r, c] for r, c in list(pacificSet & atlanticSet)]
        
