class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'R':
                    rookR = r
                    rookC = c
                    break
        
        capture = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dr, dc in directions:
            nr, nc = rookR + dr, rookC + dc
            while 0 <= nr < ROWS and 0 <= nc < COLS:
                if board[nr][nc] == "B": break
                if board[nr][nc] == "p": 
                    capture += 1    
                    break
                nr += dr
                nc += dc
        return capture