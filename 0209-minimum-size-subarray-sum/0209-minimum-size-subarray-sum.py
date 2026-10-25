class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # sliding window: move right to become legal, move left to become illegal
        # record every try while legal
        total = l = 0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
            
            
