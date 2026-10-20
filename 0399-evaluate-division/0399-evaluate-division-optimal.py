class Solution:
    def calcEquation(self, equations, values, queries):
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            first, second = equation
            adj[first].append((second, values[i]))
            adj[second].append((first, 1 / values[i]))
            
        def dfs(cur, target, visited):
            if cur == target:
                return 1.0
            visited.add(cur)
            for nei, w in adj[cur]:
                if nei not in visited:
                    res = dfs(nei, target, visited)
                    if res != -1: return w * res
            return -1
        res = []
        for start, end in queries:
            if start in adj and end in adj:
                res.append(dfs(start, end, set()))
            else:
                res.append(-1)
        return res