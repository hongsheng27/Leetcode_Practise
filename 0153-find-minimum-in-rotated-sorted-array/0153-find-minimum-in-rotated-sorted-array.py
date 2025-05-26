class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[l] > nums[r] and nums[m] >= nums[l]:
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1  
        return res
        