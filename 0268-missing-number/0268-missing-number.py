class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = [i for i in range(len(nums) + 1)]
        return sum(target) - sum(nums)

        