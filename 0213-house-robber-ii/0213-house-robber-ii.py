class Solution:
    def rob(self, nums: list[int]) -> int:
        # since 0 & n - 1 adjacent, so we must chose one
        # but we don't know which should we chose to get biggest wealth
        # so we do twice and get bigger one
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        def helper(l, r):
            _nums = nums[l: r]
            dp = [0] * len(_nums)
            dp[0] = _nums[0]
            dp[1] = max(_nums[0], _nums[1])
            for i in range(2, len(_nums)):
                dp[i] = max(dp[i - 2] + _nums[i], dp[i - 1])
            return dp[-1]
        n = len(nums)
        return max(helper(0, n - 1), helper(1, n))