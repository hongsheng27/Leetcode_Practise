class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            # recursion case
            for j in range(len(nums)):
                if used[j]: continue
                used[j] = True
                path.append(nums[j])
                backtrack(path)
                used[j] = False
                path.pop()
        backtrack([])
        return res