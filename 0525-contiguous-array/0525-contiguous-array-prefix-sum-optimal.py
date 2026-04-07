class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        res = 0
        curSum = 0

        for r in range(len(nums)):
            curSum += -1 if nums[r] == 0 else 1

            if curSum in count:
                l = count[curSum]
                res = max(res, r - l)
            else:
                count[curSum] = r
        return res
            

        
        