class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # multi-bfs from 0
        # pick small number when step on 1
        ROWS, COLS = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        round = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == -1:
                        mat[nr][nc] = round
                        q.append((nr, nc))
            round += 1
        return mat
       