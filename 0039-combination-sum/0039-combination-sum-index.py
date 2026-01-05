class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curList = []
        def dfs(j, curSum):
            print(curList, sum(curList))
            if curSum == target:
                res.append(curList.copy())
                return
            if curSum > target:
                return

            for i in range(j, len(candidates)):
                # decision to include c
                c = candidates[i]
                curList.append(c)
                dfs(i, curSum + c)
                curList.pop()
                # decision to not include c
                
        dfs(0, 0)
        return res

        
