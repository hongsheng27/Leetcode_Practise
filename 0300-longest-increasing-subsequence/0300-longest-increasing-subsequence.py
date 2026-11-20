class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                include = 1
                if nums[i] < nums[j]:
                    include += dp[j]
                    dp[i] = max(dp[i], include)
        return max(dp)
        