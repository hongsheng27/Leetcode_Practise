class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = suffix[len(nums) - 1] = 1
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            prefix[i] = p
        p = 1
        for i in range(len(nums) - 2, -1, -1):
            p *= nums[i + 1]
            suffix[i] = p
        res = [x * y for x, y in zip(prefix, suffix)]
        return res
            


        