class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for n in range(len(nums) + 1):
            if n not in num_set:
                return n

        