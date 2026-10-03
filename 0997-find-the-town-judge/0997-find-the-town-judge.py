class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # all => judge
        # traverse: t[1] all the same, find judge
        # set() - judge, traverse, if t[0]in set, remove it
        # return len set() == 0
        # 10: 10)
        # 2. find judge whose indgree = n - 1
        #judge can't see other

        # judge = trust[0][1]
        # for t in trust:
        #     if judge != t[1]:
        #         return -1
        # print('should be 2', judge)
        # seen = set()
        # for t in trust:
        #     seen.add(t[0])
        # if judge in seen:
        #     seen.remove(judge)
        # print('should be 1', seen)
        # for t in trust:
        #     if t[0] in seen:
        #         seen.remove(t[0])
        # if len(seen) != 0: return -1
        # return judge

        # restart
        if n == 1 and not trust: return 1
        judge = None
        indegree = [0] * (n + 1)
        for other, j in trust:
            indegree[j] += 1
        for i, num in enumerate(indegree):
            if num == n - 1:
                judge = i
                break
        if not judge: return -1
        for t in trust:
            if t[0] == judge:
                return -1
        return judge
            
        

       
        