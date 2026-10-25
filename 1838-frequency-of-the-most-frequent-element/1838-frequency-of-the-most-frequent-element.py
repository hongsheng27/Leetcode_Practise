class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # sliding window, but need sort, so that move right van find bigger target to satify
        # move right until illegal(bigger than k)
        # stop and move left until legal
        # record length
        nums.sort()
        res = l = total = 0
        for r in range(len(nums)):
            total += nums[r]
            while nums[r] * (r - l + 1) - total > k:
                total -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res
        