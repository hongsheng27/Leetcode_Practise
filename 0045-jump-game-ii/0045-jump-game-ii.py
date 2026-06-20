class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = curEnd = jumps = 0
        for i in range(len(nums) - 1):
            j = nums[i]
            farthest = max(farthest, i + j)
            if i == curEnd:
                curEnd = farthest
                jumps += 1
        return jumps
            

            
