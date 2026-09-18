class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            right = float('-inf') if m == len(nums) - 1 else nums[m + 1]
            left = float('-inf') if m == 0 else nums[m - 1]
            if left < nums[m] > right:
                return m
            elif nums[m] < right:
                l = m + 1
            else:
                r = m - 1