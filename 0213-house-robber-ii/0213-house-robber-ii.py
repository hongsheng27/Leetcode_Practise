class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp = [0, 0]
            for n in nums:
                tmp = dp[1]
                dp[1] = max(dp[0] + n, dp[1])
                dp[0] = tmp
            return dp[1]
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))
        
        