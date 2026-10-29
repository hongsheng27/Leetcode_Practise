class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] => minimal number of coin
        # dp[i] = min(dp[coin] + dp[i - coin]), and dp[coin] == 1
        if amount == 0: return 0
        dp = [float('inf')] * (amount + 1)
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i > coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        print(dp)
        return -1 if dp[-1] == float('inf') else dp[-1]

