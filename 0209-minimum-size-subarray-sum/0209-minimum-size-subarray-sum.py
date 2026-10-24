class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # sliding window: move right to legal, move left until illeagal
        # each left move lead to perfect result and illegal possible
        l = total = 0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
                


        