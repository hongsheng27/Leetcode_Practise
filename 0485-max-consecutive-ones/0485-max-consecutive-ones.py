class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = res = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                res = max(res, r - l + 1)
            elif nums[r] == 0:
                l = r + 1
        return res
        