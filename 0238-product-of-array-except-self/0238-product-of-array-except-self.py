class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        prefix = [1] * lenN
        suffix = [1] * lenN
        res = []
        for i in range(1, lenN):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(lenN - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(lenN):
            res.append(prefix[i] * suffix[i])
        return res

   


        