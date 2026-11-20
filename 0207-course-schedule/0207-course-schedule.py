class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = set()
        def dfs(course):
            if course in visited: return False
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei): return False
            visited.remove(course)
            adj[course] = []
            return True
        
        for i in range(numCourses):
            if adj[i]:
                if not dfs(i):
                    return False
        return True