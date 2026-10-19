class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # a -> b -> c
        # adj list, each query doing one dfs(), not sure if it have effeciency probem
        # 12:00
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        reachable = defaultdict(set)
        def dfs(course, destination, visited):
            if course == destination: 
                reachable[destination].update(visited)
                return True
            visited.add(course)
            for nei in adj[course]:
                if nei not in visited:
                    if dfs(nei, destination,visited):
                        return True
            return False

        res = []
        for pre, crs in queries:
            if crs in reachable:
                res.append(pre in reachable[crs])
            else:
                res.append(dfs(pre, crs, set()))
        return res
        # 17:26