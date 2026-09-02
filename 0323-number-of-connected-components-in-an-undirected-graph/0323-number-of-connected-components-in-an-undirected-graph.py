class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1] * n
        res = n

        def find(num):
            while num != parents[num]:
                num = parents[num]
            return num
        def union(x, y):
            nonlocal res
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            
            parents[rootY] = rootX
            size[rootX] += size[rootY]
            res -= 1
            return True
           
        for x, y in edges:
            union(x, y)

        return res