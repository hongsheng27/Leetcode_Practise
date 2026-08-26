class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        count = {0: 1}
        res = 0
        for r in range(len(nums)):
            curSum = prefix[-1] + nums[r]
            prefix.append(curSum)
            if prefix[r + 1] - k in count:
                res += count[prefix[r + 1] - k]
            count[curSum] = count.get(curSum, 0) + 1
        return res
            
