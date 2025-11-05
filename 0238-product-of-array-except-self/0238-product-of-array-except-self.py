class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            prefix[i] = p
        p = 1
        for j in range(len(nums) - 2, -1, -1):
            p *= nums[j + 1]
            suffix[j] = p
        res = [x * y for x, y in zip(prefix, suffix)]
        return res
            


        