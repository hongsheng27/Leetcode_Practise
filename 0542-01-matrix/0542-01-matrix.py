class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = [[0] * COLS for _ in range(ROWS)] 
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    res[r][c] = float('inf')
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                        mat[nr][nc] == 0 or res[row][col] + 1 >= res[nr][nc]): continue
                    q.append((nr, nc))
                    res[nr][nc] = res[row][col] + 1
           
        return res
            