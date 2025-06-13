class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        print(pref, suff)
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        
        
            


        