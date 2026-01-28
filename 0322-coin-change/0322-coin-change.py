class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            nextDp = dp
            for j in range(len(dp)):
                skip = dp[j]
                include = float('inf')
                if j - coins[i] >= 0:
                    include = 1 + dp[j - coins[i]]
                nextDp[j] = min(skip, include)
            dp = nextDp
        return dp[-1] if dp[-1] != float('inf') else -1