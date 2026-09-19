class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if r < 2 or nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l