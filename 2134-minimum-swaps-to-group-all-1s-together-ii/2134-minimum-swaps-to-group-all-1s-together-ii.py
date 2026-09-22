class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        amount = sum(nums)
        n = len(nums)
        nums = nums + nums
        windowSum = 0
        res = float('inf')
        l = 0
        for i in range(amount):
            windowSum += nums[i]
        res = min(res, amount - windowSum)
        for l in range(1, n):
            r = l + amount - 1
            windowSum += nums[r] 
            windowSum -= nums[l - 1]
            l += 1
            res = min(res, amount - windowSum)
        return res
