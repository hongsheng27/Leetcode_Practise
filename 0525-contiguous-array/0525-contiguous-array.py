class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pMap = {0: -1}
        res = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += -1 if nums[r] == 0 else 1

            if curSum in pMap:
                l = pMap[curSum]
                res = max(res, r - l)
            else:
                pMap[curSum] = r
        return res
            

