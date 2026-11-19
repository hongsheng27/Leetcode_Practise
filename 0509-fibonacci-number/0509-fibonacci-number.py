class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i in cache: return cache[i]
            
            if i == 0: return 0
            if i == 1: return 1
            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]
        return dfs(n)
