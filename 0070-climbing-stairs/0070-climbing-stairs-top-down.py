class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(total, cache):
            if total == n:
                return 1
            if total > n:
                return 0
            if total in cache: return cache[total]

            cache[total] = dfs(total + 1, cache) + dfs(total + 2, cache)
            return cache[total]
        return dfs(0, {})