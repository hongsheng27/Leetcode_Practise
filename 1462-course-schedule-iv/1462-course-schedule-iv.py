class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # a -> b -> c
        # adj list, each query doing one dfs(), not sure if it have effeciency probem
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        reachable = defaultdict(set)
        def dfs(course, root, visited):
            visited.add(course)
            reachable[root].add(course)
            for nei in adj[course]:
                if nei not in visited:
                    dfs(nei, root,visited)
        for i in range(numCourses):
            dfs(i, i, set())
        res = []
        for pre, crs in queries:
            if pre in reachable:
                res.append(crs in reachable[pre])
        return res
