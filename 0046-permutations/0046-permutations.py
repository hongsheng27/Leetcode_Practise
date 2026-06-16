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
            for i in range(len(nums)):
                if used[i]: continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res