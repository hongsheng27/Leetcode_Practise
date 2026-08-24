class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ROWS, COLS = m, n
        board = [["."] * COLS for _ in range(ROWS)]
        res = ROWS * COLS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r, c in guards:
            board[r][c] = "G"
            res -= 1
        for r, c in walls:
            board[r][c] = "W"
            res -= 1

        guardedSet = set()
        def helper(r, c, isGuard):
            if board[r][c] == "G": 
                isGuard = True
            elif board[r][c] == "W":
                isGuard = False
            elif isGuard and board[r][c] == ".": 
                guardedSet.add((r, c))
            return isGuard

        for r in range(ROWS):
            isGuard = False
            for c in range(COLS):
                isGuard = helper(r, c, isGuard)
        for r in range(ROWS):
            isGuard = False
            for c in range(COLS - 1, -1, -1):
                isGuard = helper(r, c, isGuard)
        for c in range(COLS):
            isGuard = False
            for r in range(ROWS):
                isGuard = helper(r, c, isGuard)
        for c in range(COLS):
            isGuard = False
            for r in range(ROWS - 1, -1, -1):
                isGuard = helper(r, c, isGuard)
        return res - len(guardedSet)
        