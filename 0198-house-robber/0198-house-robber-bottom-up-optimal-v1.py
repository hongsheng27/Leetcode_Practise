class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0] 
        dp = [0, 0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(dp[1], nums[i] + dp[0])
            dp[0] = dp[1]
            dp[1] = cur
        return dp[-1]