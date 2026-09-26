class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = l = prefix = 0
        for r in range(len(nums)):
            prefix += nums[r]
            while nums[r] * (r - l + 1) - prefix > k:
                prefix -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
            