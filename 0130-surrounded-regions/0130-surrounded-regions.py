class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # traverse the borders of the board, if cell is "O", than bfs it and change to other symbol
        # change every "O" to "X"
        # chnage other symblo to "O"
        # 3: 10
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
                
        while q:
            r, c = q.popleft()
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or board[nr][nc] != "O":
                    continue
                q.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O": 
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
