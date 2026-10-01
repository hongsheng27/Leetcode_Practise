class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            left = nums[m - 1] if m > 0 else float('-inf')
            right = nums[m + 1] if m < len(nums) - 1 else float('-inf')
            if left < nums[m] > right:
                return m
            if right > nums[m]:
                l = m + 1
            else:
                r = m - 1

