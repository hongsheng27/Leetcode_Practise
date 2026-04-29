class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                r = m
        if nums[l] != target: return [-1, -1]
        start = l
        
        l = 0 
        r = len(nums) - 1
        res = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        end = res - 1 if res != float('inf') else len(nums) - 1
        return [start, end]
        
