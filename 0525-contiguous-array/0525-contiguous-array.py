class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # using prefix instead sliding window, cuz moving window can't guarentee legal
        # using prefix can calculate contiguous subarray at O(n)
        # need to save {balance:  minimal position}
        # 13: 17
        seen = {0: -1}
        balance = 0
        res = 0
        for r in range(len(nums)):
                if nums[r] == 0:
                    balance -= 1
                else:
                    balance += 1
                
                if balance in seen:
                    l = seen[balance]
                    res = max(res, r - l)
                
                if balance not in seen:
                    seen[balance] = r
        return res
                


       