class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            maxCount = max(maxCount, count)
        return maxCount
        