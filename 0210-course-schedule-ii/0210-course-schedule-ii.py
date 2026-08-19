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
            course = q.popleft()
            res.append(course)
            for crs in adj[course]:
                indegree[crs] -= 1
                if not indegree[crs]:
                    q.append(crs)
        if len(res) != numCourses: return []
        return res