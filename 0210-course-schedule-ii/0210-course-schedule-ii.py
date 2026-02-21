class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { n: [] for n in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        res = []
        visitd, path = set(), set()

        def dfs(courseNum):
            if courseNum in path: return False
            if courseNum in visitd: return True
            
            path.add(courseNum)
            for child in adj[courseNum]:
                if not dfs(child):
                    return False
            path.remove(courseNum)
            visitd.add(courseNum)
            res.append(courseNum)
            return True
            
        for n in range(numCourses):
            if not dfs(n): return []
        res.reverse()
        return res
        