class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n:
                return 0
            if (r, c) in cache: return cache[(r, c)] 
            if r == m - 1 and c == n -1:
                return 1
            cache[(r, c)] = (dfs(r + 1, c) + 
                             dfs(r, c + 1))
            return cache[(r, c)] 
        return dfs(0, 0)
        