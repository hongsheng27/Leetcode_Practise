class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[pre].append(course)

        visit = set()
        def hasCycle(node):
            if not adj[node]: return False
            if node in visit: return True

            visit.add(node)
            for nei in adj[node]:
                if hasCycle(nei): return True
            visit.remove(node)
            adj[node] = []
            return False
            
        for i in range(numCourses):
            if hasCycle(i): 
                return False
        return True
           
            

        