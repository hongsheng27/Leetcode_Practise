class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeroAmount = total = maxTotal = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0: zeroAmount += 1
           
            while zeroAmount > 1:
                if nums[l] == 0: zeroAmount -= 1
                l += 1
   
            maxTotal = max(r - l, maxTotal)
        return maxTotal

