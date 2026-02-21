class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        output = []
        cycle, visit = set(), set()
        def dfs(node):
            if node in cycle: return False
            if node in visit: return True

            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei): return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return output
          