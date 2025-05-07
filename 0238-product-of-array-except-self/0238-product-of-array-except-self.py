class Solution(object):
    def productExceptSelf(self, nums):
        perfix_arr = []
        prefix_product = 1
        for num in nums:
            prefix_product *= num
            perfix_arr.append(prefix_product)
        
        suffix_arr = []
        suffix_product = 1
        for num in reversed(nums):
            suffix_product *= num
            suffix_arr.append(suffix_product)
        suffix_arr.reverse()
        
        res = []
        for i in range(len(nums)):
            prev = perfix_arr[i-1] if i > 0 else 1
            suf = suffix_arr[i+1] if i < len(nums) - 1 else 1
            res.append(prev * suf)
        print(res)
        return res

        
            


        