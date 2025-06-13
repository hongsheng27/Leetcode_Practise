class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        prefix = 1
        for i in range(n):
            pref[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            suff[i] = suffix
            suffix *= nums[i]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        
        
            


        