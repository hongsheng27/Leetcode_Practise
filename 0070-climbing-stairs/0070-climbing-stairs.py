class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] => how many ways to i
        # dp[i] = (dp[i - 2] + dp[2]) + (dp[i - 1] + dp[1]) - 1
        if n == 1: return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] += dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[-1]