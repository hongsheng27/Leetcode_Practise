class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # x ^ 0 = x
        # x ^ x = 0
        res = 0
        for num in nums:
            res ^= num
        for i in range(len(nums) + 1):
            res ^= i
        return res