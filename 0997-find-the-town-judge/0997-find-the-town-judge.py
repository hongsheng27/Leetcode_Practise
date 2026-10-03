class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        outdegree = [0] * (n + 1)
        indegree = [0] * (n + 1)

        for t in trust:
            outdegree[t[0]] += 1
            indegree[t[1]] += 1
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1