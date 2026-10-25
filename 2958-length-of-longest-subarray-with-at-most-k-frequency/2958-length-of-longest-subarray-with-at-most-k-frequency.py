class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window: move right to get logner subarray until illegal
        # move left to be come legal, move left can must decrease target[freq]
        # record ans while legal
        # use map to calculate freq
        # 04:10
        res = l = 0
        count = defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]] += 1

            while count[nums[r]] > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0: del count[nums[l]]
                l += 1

            res = max(res, r - l + 1)
        return res

