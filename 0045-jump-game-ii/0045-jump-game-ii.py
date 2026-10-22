class Solution:
    def jump(self, nums: list[int]) -> int:
        # furtherest to record furtherest this round
        # border means end of this round, when reaching, border = furtherest
        border = 0
        furtherest = 0
        steps = 0
        for i in range(len(nums) - 1):
            furtherest = max(furtherest, i + nums[i])
            if i == border:
                border = furtherest
                steps += 1
        return steps