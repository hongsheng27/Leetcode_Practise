class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                used[i] = False
                path.pop()
        backtrack([])
        return res