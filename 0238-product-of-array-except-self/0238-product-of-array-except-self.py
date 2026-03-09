class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        res = [1] * lenN
        p = 1
        for i in range(1, lenN):
            p *= nums[i - 1]
            res[i] = p
        p = 1
        for i in range(lenN - 2, -1, -1):
            p *= nums[i + 1]
            res[i] = res[i] * p
        return res

   


        