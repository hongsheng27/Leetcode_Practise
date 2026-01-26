class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        cache = [[-1] * (amount + 1) for _ in range(N)]
        def dfs(i, total):
            if total == amount:
                return 0
            if total > amount or i >= len(coins):
                return float('inf')
            if cache[i][total] != -1: return cache[i][total]
            # skip
            res1 = dfs(i + 1, total)
            # not skip
            res2 = 1 + dfs(i, total + coins[i])
            cache[i][total] =  min(res1, res2)
            return cache[i][total]
        result = dfs(0, 0)
        return result if result != float('inf') else -1