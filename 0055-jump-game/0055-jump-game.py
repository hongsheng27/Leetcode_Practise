class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(index):
            if not index: return True
            for i in range(index - 1, -1, -1):
                if nums[i] + i >= index:
                    return dfs(i)
            return False
        return dfs(len(nums) - 1)


                
        