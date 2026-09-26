class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = l = windowSum = 0
        for r in range(len(nums)):
            windowSum += nums[r]
            while nums[r] * (r - l + 1) - windowSum > k:
                windowSum -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
            