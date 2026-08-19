class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    q.append((r, c))
                    visit.add((r, c))
        pacific = []
        while q:
            row, col = q.popleft()
            pacific.append((row, col))
            for dr, dc in neighbors:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS
                    or (nr, nc) in visit or heights[nr][nc] < heights[row][col]): continue
                visit.add((nr, nc))
                q.append((nr, nc))
        

        q = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1:
                    q.append((r, c))
                    visit.add((r, c))
        atlantic = []
        while q:
            row, col = q.popleft()
            atlantic.append((row, col))
            for dr, dc in neighbors:
                nr, nc = row + dr, col + dc
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS
                    or (nr, nc) in visit or heights[nr][nc] < heights[row][col]): continue
                visit.add((nr, nc))
                q.append((nr, nc))
        
        total = set(pacific + atlantic)
        single = set(pacific)
        for a in atlantic:
            if a in single:
                single.remove(a)
            else:
                single.add(a)
        res = []
        for t in list(total):
            if t not in single:
                res.append(t)
        return res


