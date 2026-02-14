class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or visited[r][c]: return False

            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)
                  )
            visited[r][c] = False
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
        

        