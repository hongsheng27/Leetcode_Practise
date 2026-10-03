class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # 2. find judge whose indgree = n - 1
        #judge can't see other

        if n == 1 and not trust: return 1
        judge = None
        indegree = [0] * (n + 1)
        for other, j in trust:
            indegree[j] += 1
        for i, num in enumerate(indegree):
            if num == n - 1:
                if not judge:
                    judge = i
                else:
                    return -1
        if not judge: return -1
        for t in trust:
            if t[0] == judge:
                return -1
        return judge

            
        

       
        