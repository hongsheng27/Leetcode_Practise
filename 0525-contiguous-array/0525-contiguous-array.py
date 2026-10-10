class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = []
        balance = 0
        for n in nums:
            if n == 0:
                balance -= 1
            else:
                balance += 1
            prefix.append(balance)
        print(prefix)
        pMap = {0: -1}
        res = 0
        for r in range(len(prefix)):
            if prefix[r] in pMap:
                res = max(res, r - pMap[prefix[r]])
            if prefix[r] not in pMap:
                pMap[prefix[r]] = r
        return res
            

