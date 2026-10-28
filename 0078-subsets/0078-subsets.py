class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path)
            path.remove(nums[i])

            dfs(i + 1, path)
        dfs(0, [])
        return res