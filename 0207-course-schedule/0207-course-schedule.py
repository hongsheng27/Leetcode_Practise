class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            for crs in adj[course]:
                indegree[crs] -= 1
                if not indegree[crs]:
                    q.append(crs)
        return max(indegree) == 0



        