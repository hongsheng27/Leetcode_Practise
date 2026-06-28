class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        def dfs(r, c, index):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                (r, c) in visited or board[r][c] != word[index]):
                 return False
            if index == len(word) - 1: return True
            visited.add((r, c))
            result = (dfs(r + 1, c, index + 1) or
                      dfs(r - 1, c, index + 1) or
                      dfs(r, c + 1, index + 1) or
                      dfs(r, c - 1, index + 1))
            visited.remove((r, c))
            return result
        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0): return True
        return False
        