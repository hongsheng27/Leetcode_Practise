class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        res = [nums[-1], len(nums) - 1] # value, index
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        pivot = r
        
        if target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


            
        


        