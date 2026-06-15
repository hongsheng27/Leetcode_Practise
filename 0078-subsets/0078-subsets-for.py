class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, stack):
            # base case
            res.append(stack.copy())
            # recursion case
            for i in range(index, len(nums)):
                stack.append(nums[i])
                backtrack(i + 1, stack)
                stack.pop()

        backtrack(0, [])
        return res

        