class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, s, path):
            if s == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or s > target: return
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                backtrack(j, s + candidates[j], path)
                path.pop()

        backtrack(0, 0, [])
        return res