class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = curFar = steps = 0
        for i in range(len(nums) - 1):
            curFar = max(curFar, i + nums[i])
            if i == farthest:
                farthest = curFar
                steps += 1
        return steps
