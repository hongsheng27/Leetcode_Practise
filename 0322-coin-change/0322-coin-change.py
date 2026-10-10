class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # solution1 : dp
        # dp[i] = min(1 + dp[i - coin])
        # 2: 40
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = float('inf')
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[-1] == float('inf') else dp[-1]
