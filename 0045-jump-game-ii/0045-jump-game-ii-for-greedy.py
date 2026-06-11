class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        curEnd = 0
        jumps = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == curEnd:
                jumps += 1
                curEnd = farthest
        return jumps




        