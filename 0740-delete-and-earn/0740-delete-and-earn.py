class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # list [0, 0, 4, 9, 4]
        # dp[i] = maximal point from 0 to i
        # dp[i] = max(dp[i - 2] + list[i], dp[i - 1])
        # return dp[-1]
        # 11:10
        if len(nums) == 1: return nums[0]
        
        maxVal = max(nums)
        dp = [0] * (maxVal + 1)
        point = [0] * (maxVal + 1)
        
        for num in nums:
            point[num] += num
        
        dp[1] = point[1]
        for i in range(2, maxVal + 1):
            dp[i] = max(dp[i - 2] + point[i], dp[i - 1])
        return dp[-1]
       