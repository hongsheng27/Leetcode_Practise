class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            # base case
            if i >= len(nums):
                subSets.append(curSet.copy())
                return
            # include nums[i]
            curSet.append(nums[i])
            dfs(i + 1)

            # not include nums[i]
            curSet.pop()
            dfs(i + 1)
        subSets, curSet = [], []
        dfs(0)
        return subSets

        