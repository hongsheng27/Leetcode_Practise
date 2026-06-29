class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = float('-inf')
        for num in nums:
            total = max(total, 0)
            total += num
            maxSum = max(total, maxSum)
        return maxSum
        