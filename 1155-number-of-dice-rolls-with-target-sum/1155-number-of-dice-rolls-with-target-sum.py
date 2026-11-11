class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dfs with memo
        MOD = 10 ** 9 + 7
        cache = {}
        def dfs(total, limit):
            if (total, limit) in cache: return cache[(total, limit)]
            if total == target and limit == 0:
                return 1
            if total > target or limit <= 0:
                return 0
            res = 0
            for i in range(1, k + 1):
                res += dfs(total + i, limit - 1)
            cache[(total, limit)] = res % MOD
            return cache[(total, limit)]
        return dfs(0, n)