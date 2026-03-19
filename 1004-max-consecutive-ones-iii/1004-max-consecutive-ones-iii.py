class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = l = res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0: zeros -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        