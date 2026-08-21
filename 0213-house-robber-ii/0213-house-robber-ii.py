class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n <= 2: return max(nums[0], nums[1])
        def rob(l, r):
            dp = [0, 0]
            dp[0] = nums[l]
            dp[1] = max(nums[l], nums[l + 1])

            for i in range(l + 2, r + 1):
                cur = max(dp[1], nums[i] + dp[0])
                dp[0] = dp[1]
                dp[1] = cur
            return dp[-1]
        return max(rob(0, n - 2), rob(1, n - 1))