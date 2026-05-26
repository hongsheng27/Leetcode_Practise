class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr

        