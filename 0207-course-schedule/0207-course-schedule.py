class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        q = deque()
        for i, ind in enumerate(indegree):
            if ind == 0:
                q.append(i)
        while q:
            crs = q.popleft()
            numCourses -= 1
            for course in adj[crs]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return numCourses == 0
