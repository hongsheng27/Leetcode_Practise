class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                used[i] = False
                path.pop()
        backtrack([])
        return res