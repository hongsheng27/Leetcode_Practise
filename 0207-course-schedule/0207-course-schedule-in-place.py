class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for n in range(numCourses):
            adj[n] = []
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        def dfs(node, path):
            if not adj[node]: return True
            if node in path: return False
            path.add(node)
            for child in adj[node]:
                if not dfs(child, path):
                    return False

            adj[node] = []
            path.remove(node)
            return True

        for n in range(numCourses):
            if not dfs(n, set()): return False
        return True
            

        