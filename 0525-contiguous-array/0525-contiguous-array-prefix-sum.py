class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        newNums = []
        for n in nums:
            if n == 0: n = -1
            newNums.append(n)
        prefix = [0]
        count = {0: -1}
        res = 0

        for r in range(len(newNums)):
            curSum = prefix[-1] + newNums[r]
            prefix.append(curSum)

            if curSum in count:
                l = count[curSum]
                res = max(res, r - l)
            else:
                count[curSum] = r
        return res
            

        
        