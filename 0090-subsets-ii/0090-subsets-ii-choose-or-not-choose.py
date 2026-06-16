class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            # decision to include nums[i]
            curSet.append(nums[i])
            dfs(i + 1)
            # decision to NOT include nums[i]
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res
        