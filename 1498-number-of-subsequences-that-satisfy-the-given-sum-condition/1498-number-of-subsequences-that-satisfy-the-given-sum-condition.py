class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 2 ** (r - l)
                l += 1
            else:
                r -= 1
        return res % (10 ** 9 + 7)

     