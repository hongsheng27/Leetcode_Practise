class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] => minimal number of sum of perfect square
        # dp[i] = 1 + dp[i - perfect]
        # use O(n) to find all perfect number
        # tc will be O(n * P), I don't know how to cal O(P), but p might be log n, n = 10^4 should be find
        perfects = []
        start = 1
        while start * start <= n:
            perfects.append(start * start)
            start += 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, (n + 1)):
            for perfect in perfects:
                if i >= perfect:
                    dp[i] = min(dp[i], 1 + dp[i - perfect])
        return dp[-1]