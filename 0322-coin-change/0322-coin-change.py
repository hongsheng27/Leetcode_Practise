class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        dp = [float('inf')] * (amount + 1)
        for i in range(amount + 1):
            for coin in coins:
                if coin == i:
                    dp[i] = 1
                elif i - coin > 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[-1] == float('inf') else dp[-1]

