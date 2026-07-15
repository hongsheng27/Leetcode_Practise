class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def backtrack(r, c, index):
            # base case
            if index == len(word): return True
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visited or board[r][c] != word[index]):
                return False
            # recursion case
            visited.add((r, c))
            res = (backtrack(r + 1, c, index + 1) or
                   backtrack(r - 1, c, index + 1) or
                   backtrack(r, c + 1, index + 1) or
                   backtrack(r, c - 1, index + 1))
            visited.remove((r, c))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        return False