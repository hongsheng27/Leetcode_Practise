class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = f = 0
        while f < len(nums):
            if nums[f] != nums[s]:
                s += 1
                nums[s] = nums[f]
            f += 1
        return s + 1

        