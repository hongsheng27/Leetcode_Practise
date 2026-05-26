class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for n in range(len(nums) + 1):
            if n not in seen:
                return n

        