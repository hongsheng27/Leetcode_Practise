class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin == i:
                    dp[i] = 1
                elif i - coin > 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == float('inf') else dp[amount]

