class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        cost = 0
        res = 1
        windowSum = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            cost = nums[r] * (r - l + 1) - windowSum
            while cost > k:
                windowSum -= nums[l]
                cost -= (nums[r] - nums[l])
                l += 1
            res = max(res, r - l + 1)
        return res
            
                
