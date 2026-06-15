class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, stack):
            # base case
            if index == len(nums):
                res.append(stack.copy())
                return
            # recursion case
            stack.append(nums[index])
            backtrack(index + 1, stack)
            stack.pop()

            backtrack(index + 1, stack)

        backtrack(0, [])
        return res

        