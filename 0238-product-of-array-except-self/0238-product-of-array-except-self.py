class Solution(object):
    def productExceptSelf(self, nums):
        perfix = []
        prefix_product = 1
        for num in nums:
            prefix_product *= num
            perfix.append(prefix_product)
        
        suffix = []
        suffix_product = 1
        for num in reversed(nums):
            suffix_product *= num
            suffix.append(suffix_product)
        suffix.reverse()
        
        res = []
        for i in range(len(nums)):
            pref = perfix[i-1] if i > 0 else 1
            suf = suffix[i+1] if i < len(nums) - 1 else 1
            res.append(pref * suf)
        return res

        
            


        