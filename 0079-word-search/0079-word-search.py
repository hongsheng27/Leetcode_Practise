class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def backtrack(row, col, i):
            # base case
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row == ROW or col == COL
                or (row, col) in visited or board[row][col] != word[i]):
                return False
            visited.add((row, col))
            for nr, nl in neighbors:
                if backtrack(row + nr, col + nl, i + 1):
                    return True
            visited.remove((row, col))
            return False
          
        for i in range(ROW):
            for j in range(COL):
                if backtrack(i, j, 0): 
                    return True
        return False