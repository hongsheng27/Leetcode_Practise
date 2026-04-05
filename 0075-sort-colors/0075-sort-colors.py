class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = i = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
