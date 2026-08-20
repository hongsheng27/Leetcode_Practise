class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            isSurrend = True
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            res = []
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                res.append((row, col))
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS):
                        isSurrend = False
                        continue
                    if ((nr, nc) in visited or board[nr][nc] == "X"): continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            if isSurrend:
                for r, c in res:
                    board[r][c] = "X"     

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c)

        