class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dfs with memo # (total, dice)
        # tc: O(n * k * n) sc: O(n * k * n)
        MOD = 10 ** 9 + 7
        cache = {} # (total, dice)
        def dfs(total, dice):
            if (total, dice) in cache: return cache[(total, dice)]
            if dice == 0: return 1 if total == target else 0 
            if dice < 0 or total > target:
                return 0
            res = 0
            for i in range(1, k + 1):
                res += dfs(total + i, dice - 1)
            cache[(total, dice)] = res % MOD
            return cache[(total, dice)]
        
        return dfs(0, n)