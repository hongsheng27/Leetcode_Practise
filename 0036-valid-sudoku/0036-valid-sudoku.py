class Solution(object):
    def isValidSudoku(self, board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if (val in rows[row] or val in cols[col] or val in squares[(col // 3, row // 3)]):
                    return False
                rows[row].add(val)
                cols[col].add(val)
                squares[(col // 3, row // 3)].add(val)


        return True

        