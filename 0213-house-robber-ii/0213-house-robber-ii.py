class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def r(nums):
            dp = [0, 0]
            for n in nums:
                tmp = dp[1]
                dp[1] = max(dp[0] + n, dp[1])
                dp[0] = tmp
            return dp[1]
        return max(r(nums[:-1]), r(nums[1:]))
        
        