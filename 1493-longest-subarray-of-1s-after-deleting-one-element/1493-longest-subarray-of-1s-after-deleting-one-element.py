class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # solution1: sliding window
        # condition: over one zero and shrink
        # window size = window size - 1
        l = res = 0
        count = {0: 0, 1: 0}
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[0] > 1:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res

        