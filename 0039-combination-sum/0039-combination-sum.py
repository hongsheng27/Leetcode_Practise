class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, s, path):
            if s == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or s > target: return
            path.append(candidates[i])
            backtrack(i, s + candidates[i], path)
            path.pop()

            backtrack(i + 1, s, path)
        backtrack(0, 0, [])
        return res