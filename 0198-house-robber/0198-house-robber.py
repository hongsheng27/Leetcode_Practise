class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for i in range(len(nums)):
            tmp = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[-1]
