class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        q = deque()
        visited = set()
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)
                visited.add(i)
        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            for nei in adj[crs]:
                if nei in visited: return
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    visited.add(nei)
        return finished == numCourses
        
