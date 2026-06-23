class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, path):
            # base case
            if i == len(nums):
                res.append(path.copy())
                return
            # recursion case
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
