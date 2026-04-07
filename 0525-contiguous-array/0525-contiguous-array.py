class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        newNums = []
        for n in nums:
            if n == 0: n = -1
            newNums.append(n)
        prefix = [0]
        count = {0: 0}
        res = 0

        for r in range(len(newNums)):
            curSum = prefix[-1] + newNums[r]
            prefix.append(curSum)

            if curSum in count:
                l = count[curSum]
                res = max(res, r + 1 - l)

            if curSum not in count:
                count[curSum] = r + 1
            else:
                count[curSum] = min(count[curSum], r + 1)
        return res
            

        
        