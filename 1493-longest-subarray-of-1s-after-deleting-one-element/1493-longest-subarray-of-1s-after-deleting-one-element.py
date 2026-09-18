class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeroAmount = total = maxTotal = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0: zeroAmount += 1
            elif nums[r] == 1: total += 1
            while zeroAmount > 1:
                if nums[l] == 0: zeroAmount -= 1
                elif nums[l] == 1: total -= 1
                l += 1
            final = total - 1 if zeroAmount == 0 else total
            maxTotal = max(final, maxTotal)
        return maxTotal

