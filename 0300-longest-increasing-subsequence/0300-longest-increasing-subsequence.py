class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)
        dp[-1] = 1

        for i in range(len(nums) - 1, -1, -1):
            maxVlue = 1
            for j in range(i + 1, len(nums)):
                include = 1
                if nums[i] < nums[j]:
                    include += dp[j]
                    maxVlue = max(maxVlue, include)
            dp[i] = maxVlue
        return max(dp[i] for i in range(len(nums)))
        