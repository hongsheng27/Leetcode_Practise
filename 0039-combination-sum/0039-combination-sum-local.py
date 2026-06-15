class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curList = []
        def dfs(i, total):
            if total == target:
                res.append(curList.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # decision to include candidates[i]
            curList.append(candidates[i])
            dfs(i, total + candidates[i])
            # decision to NOT include candidates[i]
            curList.pop()
            dfs(i + 1, total)
        dfs(0, 0) 
        return res

        
