class Solution: 
    def removeDuplicates(self, nums: List[int]) -> int: 
        seen = set() 
        l = 0 
        for r in range(len(nums)):
            if nums[r] not in seen: 
                nums[l] = nums[r] 
                l += 1 
                seen.add(nums[r]) 
        return l