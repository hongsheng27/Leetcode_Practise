class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        size = [1] * n
        count = n

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            nonlocal count
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB: 
                return False

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            count -= 1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        return count == 1