class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(v):
            while v != parent[v]:
                v = parent[v]
            return v
        def union(v1, v2):
            v1Root = find(v1)
            v2Root = find(v2)
            
            if v1Root == v2Root:
                return False

            if size[v1Root] < size[v2Root]:
                v1Root, v2Root = v2Root, v1Root
            parent[v2Root] = parent[v1Root]
            size[v1Root] += size[v2Root]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
