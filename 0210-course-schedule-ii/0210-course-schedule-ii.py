class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # solution1: like course schedule I, just need to save visited node and reutrn it
        # 02:30
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
                