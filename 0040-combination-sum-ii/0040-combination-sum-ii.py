class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, total, path):
            if total == target:
                res.append(path.copy())
                return
            if total > target or i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                backtrack(j + 1, total + candidates[j], path)
                path.pop()
        backtrack(0, 0, [])
        return res