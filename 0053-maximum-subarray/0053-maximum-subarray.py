class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxSum = float('-inf')
        for n in nums:
            total += n
            maxSum = max(maxSum, total)
            total = max(0, total)
        return maxSum
            

        