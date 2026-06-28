class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        def backtrack(row, col, i):
            # base case
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row == ROW or col == COL
                or (row, col) in visited or board[row][col] != word[i]):
                return False
            visited.add((row, col))
            res = (backtrack(row + 1, col, i + 1) or 
                    backtrack(row - 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row, col - 1, i + 1))
            visited.remove((row, col))
            return res
          
        for i in range(ROW):
            for j in range(COL):
                if backtrack(i, j, 0): 
                    return True
        return False