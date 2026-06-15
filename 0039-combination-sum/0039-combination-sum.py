class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, total, stack):
            # base ase
            if total == target:
                res.append(stack.copy())
                return
            if total > target or index >= len(candidates):
                return
            # recursion case
            # self
            stack.append(candidates[index])
            backtrack(index, total + candidates[index], stack)
            stack.pop()
            # nothing
            backtrack(index + 1, total, stack)
            
        backtrack(0, 0, [])
        return res