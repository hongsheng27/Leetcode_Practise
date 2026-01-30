class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3 
        cols = [0] * 3
        diag = 0
        revDiag = 0

        for i, move in enumerate(moves):
            score = 1 if i % 2 == 0 else -1
            row, col = move
            rows[row] += score
            cols[col] += score
            if row - col == 0:
                diag += score
            if row + col == 2:
                revDiag += score
            if rows[row] == 3 or cols[col] ==  3 or diag == 3 or revDiag == 3:
                return "A"
            elif rows[row] == -3 or cols[col] ==  -3 or diag == -3 or revDiag == -3:
                return "B"
        return "Pending" if len(moves) < 9 else "Draw"
        