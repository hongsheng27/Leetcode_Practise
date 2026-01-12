class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] == "X" or (r, c) in visit: return
            visit.add((r, c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            return visit
        def isSurround(connect):
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for r, c in connect:
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                        return False
            return True
        def fillX(visit):
            for r, c in visit:
                board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit: 
                    connect = dfs(r, c, set())
                    visit = visit | connect
                    if isSurround(connect): fillX(connect)
