class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            nonlocal n
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: return False

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA
            size[rootA] += size[rootB]
            n -= 1
        
        for a, b in edges:
            union(a, b)
        return n