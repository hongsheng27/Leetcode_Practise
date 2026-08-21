class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for n in nums:
            tmp = max(dp[0] + n, dp[1])
            dp[0] = dp[1] 
            dp[1] = tmp
        return dp[1]