class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        farthest = curEnd = res = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                res += 1
                curEnd = farthest
        return res
       

