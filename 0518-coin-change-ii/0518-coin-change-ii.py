class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp = [0, 1, 2, 2, 3, 4, 5]
        # dp[i] += dp[i - coin]
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i - coin]
        return dp[-1]
            

        
