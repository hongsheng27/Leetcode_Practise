class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)

        def dfs(course, visited):
            for nei in adj[course]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, visited)
            return visited

        reachable = defaultdict(set)
        for i in range(numCourses):
            reachable[i] = dfs(i, set())

        res = []
        for pre, crs in queries:
            res.append(crs in reachable[pre])
        return res
