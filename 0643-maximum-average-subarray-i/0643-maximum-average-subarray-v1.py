class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        k_sum = 0
        r = l = 0
        while r < len(nums):
            k_sum += nums[r]

            if r + 1 >= k:
                res = max(res, k_sum)
                k_sum -= nums[l]
                l += 1
            r += 1
        
        return res / k
            

            