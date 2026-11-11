class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dfs with memo
        MOD = 10 ** 9 + 7
        cache = defaultdict(int)
        def dfs(total, limit):
            if (total, limit) in cache: return cache[(total, limit)]
            if total == target and limit == 0:
                return 1
            if total > target or limit <= 0:
                return 0
        
            for i in range(1, k + 1):
                cache[(total, limit)] += dfs(total + i, limit - 1)
            return cache[(total, limit)]
        return dfs(0, n) % MOD