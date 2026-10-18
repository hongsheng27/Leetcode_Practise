class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # directed graph
        # indegree == 0 to find start, multi source bfs
        # if visited, indegree -= 1, when it become 0, put node into queue
        # return True if max(indegree) == 0
        # 10: 00
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        q = deque()
        visited = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                visited.add(i)
        while q:
            course = q.popleft()
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return max(indegree) == 0
