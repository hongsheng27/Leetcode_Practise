class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        def helper(l, r):
            if l > r: return None
            m = (l + r) // 2
            left = float('-inf') if m == 0 else nums[m - 1]
            right = float('-inf') if m == len(nums) - 1 else nums[m + 1]
            if left < nums[m] and nums[m] > right:
                return m
            
            return helper(m + 1, r) or helper(l, m - 1)
       
        return helper(l, r)