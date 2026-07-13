class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return
            # recursion case
            for i in range(len(nums)):
                if used[i] or (i > 0 and not used[i - 1] and nums[i] == nums[i - 1]): 
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                used[i] = False
                path.pop()
        backtrack([])
        return res

      