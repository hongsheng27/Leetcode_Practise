class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxTotal = float('-inf')
        for num in nums:
            total += num
            maxTotal = max(total, maxTotal)
            total = max(0, total)
        return maxTotal