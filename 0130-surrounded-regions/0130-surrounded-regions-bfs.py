class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                board[row][col] = "S"
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or
                        board[nr][nc] == "X" or (nr, nc) in visited): continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS -1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    bfs(r, c) 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"