class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, s, path):
            if s == target: 
                res.append(path.copy())
                return
            if s > target or i >= len(candidates): return
            # recursion case
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                path.append(candidates[j])
                backtrack(j + 1, s + candidates[j], path)
                path.pop()
        backtrack(0, 0, [])
        return res