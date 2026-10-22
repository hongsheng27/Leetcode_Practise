class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        total = 1
        for i in range(1, n):
            total *= nums[i - 1]
            res[i] *= total
        total = 1
        for i in range(n - 2, -1, -1):
            total *= nums[i + 1]
            res[i] *= total
        return res
        