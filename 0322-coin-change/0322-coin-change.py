class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins) + 1, amount + 1
        dp = [[float('inf')] * M for _ in range(N)]

        for r in range(N):
            dp[r][0] = 0

        for i in range(1, N):
            for j in range(1, M):
                skip = dp[i - 1][j]
                include = float('inf')
                if j - coins[i - 1] >= 0:
                    include = 1 + dp[i][j - coins[i - 1]]
                dp[i][j] = min(skip, include)
        res = dp[len(coins)][amount]
        return res if res != float('inf') else -1