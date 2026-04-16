class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0:
                nums[s] = nums[f]
                s += 1
        for i in range(s, len(nums)):
            nums[i] = 0
        

                
        