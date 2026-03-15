class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        length = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if length == float('inf') else length 
        