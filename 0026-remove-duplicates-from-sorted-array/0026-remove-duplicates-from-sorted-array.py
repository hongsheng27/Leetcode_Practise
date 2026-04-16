class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        for f in range(len(nums)):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
        return s + 1
        