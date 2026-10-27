class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] => how many ways to i
        # dp[i] += dp[i - 1] + dp[i - 2]
        dp = [0] * (n + 2)
        dp[1] = 1
        for i in range(2, n + 2):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]