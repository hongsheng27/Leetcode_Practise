class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        res = n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            nonlocal res
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            
            parent[rootY] = rootX
            size[rootX] += size[rootY]
            res -= 1
           
        for x, y in edges:
            union(x, y)

        return res