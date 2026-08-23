class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for c in coins:
            if c <= amount: dp[c] = 1
        for i in range(1, len(dp)):
            if dp[i] != 0: continue
            minValue = float('inf')
            for c in coins:
                if i > c:
                    minValue = min(dp[i - c] + 1, minValue)
            dp[i] = minValue
        return dp[-1] if dp[-1] != float('inf') else -1