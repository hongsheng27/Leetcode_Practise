class Solution:
    def jump(self, nums: List[int]) -> int:
        farEnd = edge = jump = 0
        for i in range(len(nums) - 1):
            j = nums[i]
            farEnd = max(farEnd, i + j)
            if i == edge:
                edge = farEnd
                jump += 1
        return jump
            

            
