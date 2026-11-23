class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # num, i
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i