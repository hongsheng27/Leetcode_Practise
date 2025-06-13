class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        prefix = 1
        for i in range(1, n):
            prefix *= nums[i - 1]
            pref[i] = prefix
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            suff[i] = suffix
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        
        
            


        