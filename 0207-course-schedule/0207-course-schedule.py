class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)

        visit = set()
        safe = set()
        def has_cycle(node):
            if node not in adj or node in safe:
                return False # to the end
            if node in visit:
                return True # cycle

            visit.add(node)
            for nei in adj[node]:
                if has_cycle(nei): return True
            visit.remove(node)
            safe.add(node)
            return False
            
        for i in range(numCourses):
            if has_cycle(i): 
                return False
        return True
           
            