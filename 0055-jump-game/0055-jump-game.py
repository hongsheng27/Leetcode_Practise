class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def sliceGoal(goalIndex):
            if not goalIndex: return True
            for i in range(goalIndex - 1, -1, -1):
                if nums[i] >= goalIndex - i:
                    return sliceGoal(i)
            return False
        return sliceGoal(len(nums) - 1)
        
            
        