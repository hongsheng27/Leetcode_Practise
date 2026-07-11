class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, s, path):
            # base case
            if s == target: 
                res.append(path.copy())
                return
            if s > target or i == len(candidates):
                return
            # recursion case
            path.append(candidates[i])
            backtrack(i, s + candidates[i], path)
            path.pop()

            backtrack(i + 1, s, path)

        backtrack(0, 0, [])
        return res


    