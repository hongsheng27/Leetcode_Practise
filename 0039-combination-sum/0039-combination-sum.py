class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, total, path):
            # base case
            if total == target:
                res.append(path.copy())
                return
            if total > target or index >= len(candidates):
                return
            # recursion case
            # choose candidates[index]
            path.append(candidates[index])
            backtrack(index, total + candidates[index], path)
            path.pop()
            # skip candidates[index]
            backtrack(index + 1, total, path)
            
        backtrack(0, 0, [])
        return res