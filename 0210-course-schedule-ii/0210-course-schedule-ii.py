class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        q = deque()
        for i in range(len(indegree)):
            if not indegree[i]:
                q.append(i)
        res = []
        while q:
            pre = q.popleft()
            res.append(pre)
            for crs in adj[pre]:
                indegree[crs] -= 1
                if not indegree[crs]:
                    q.append(crs)
        for d in indegree:
            if d > 0:
                return []
        return res