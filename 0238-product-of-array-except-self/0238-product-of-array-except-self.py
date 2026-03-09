class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        res = [1] * lenN
        product = 1
        for i in range(1, lenN):
            product = product * nums[i - 1]
            res[i] = product
        print(res)
        product = 1
        for i in range(lenN - 2, -1, -1):
            product = product * nums[i + 1]
            res[i] = res[i] * product
        print(res)
        return res

   


        