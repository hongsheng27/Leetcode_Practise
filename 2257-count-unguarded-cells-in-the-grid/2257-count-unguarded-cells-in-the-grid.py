class Solution:
    def countUnguarded(
        self,
        m: int,
        n: int,
        guards: List[List[int]],
        walls: List[List[int]]
    ) -> int:
        ROWS, COLS = m, n
        board = [["."] * COLS for _ in range(ROWS)]
        res = ROWS * COLS

        for r, c in guards:
            board[r][c] = "G"
            res -= 1

        for r, c in walls:
            board[r][c] = "W"
            res -= 1

        def helper(r, c):
            nonlocal res
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == "W" or board[nr][nc] == "G":
                        break

                    if board[nr][nc] == ".":
                        board[nr][nc] = "guarded"
                        res -= 1

                    nr += dr
                    nc += dc

        for r, c in guards:
            helper(r, c)

        return res