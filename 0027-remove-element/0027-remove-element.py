class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = f = 0
        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s
