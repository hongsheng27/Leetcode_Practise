class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        for f in range(len(nums)):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
        return s
        
        

        