class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        def helper(r, c):
            count = 0
            top = left = 0
            bottom = ROWS - 1
            right = COLS - 1
            for col in range(c + 1, right + 1):
                if board[r][col] == "B": break
                if board[r][col] == "p": 
                    count += 1
                    break
            for col in range(c - 1, left - 1, -1):
                if board[r][col] == "B": break
                if board[r][col] == "p": 
                    count += 1
                    break
            for row in range(r + 1, bottom + 1):
                if board[row][c] == "B": break
                if board[row][c] == "p": 
                    count += 1
                    break
            for row in range(r - 1, top - 1, -1):
                if board[row][c] == "B": break
                if board[row][c] == "p": 
                    count += 1
                    break
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'R':
                    return helper(r, c) 