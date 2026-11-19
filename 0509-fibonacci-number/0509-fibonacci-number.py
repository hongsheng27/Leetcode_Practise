class Solution:
    def fib(self, n: int) -> int:
        def dfs(i):
            if i == 0: return 0
            if i == 1: return 1

            return dfs(i - 1) + dfs(i - 2)
        return dfs(n)
