class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # thinking: longest subarray with specific condition(1 + k's not 1)
        # sliding window: move right to find longest subarray until it becomes illegal
        # move left to become legal, cal while legal
        # use (r - l + 1) - oneAmount to compare with k
        # 4: 30
        oneFreq = l = res = 0
        for r in range(len(nums)):
            if nums[r] == 1: oneFreq += 1

            while (r - l + 1) - oneFreq > k:
                if nums[l] == 1: oneFreq -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        # 7: 00

