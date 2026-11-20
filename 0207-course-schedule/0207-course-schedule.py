class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        q = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)
        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finished == numCourses
        
