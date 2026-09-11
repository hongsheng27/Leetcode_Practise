class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            tmp = max(nums[i] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[-1]
