class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent = [i for i in range(n)]
        size = [1] * n

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB: 
                return False

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        return True