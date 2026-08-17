class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            total += i * nums[i]

        totalSum = sum(nums)
        curr = maxTotal = total

        for shift in range(1, n):
            curr = curr + totalSum - n * nums[n - shift]
            maxTotal = max(curr, maxTotal)
        return maxTotal




        
        
