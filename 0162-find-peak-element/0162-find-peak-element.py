class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            left = float('-inf') if m == len(nums) - 1 else nums[m + 1]
            right = float('-inf') if m == 0 else nums[m - 1]
            if nums[m] > left and nums[m] > right:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1