class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        farthest = curEnd = res = 0
        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            print(res)
            if farthest >= len(nums) - 1: return res + 1
            if i == curEnd:
                res += 1
                curEnd = farthest
       

