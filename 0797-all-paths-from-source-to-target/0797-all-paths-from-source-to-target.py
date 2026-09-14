class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def dfs(i, path):
            if i == n - 1:
                res.append(path.copy())
                return 
            for nei in graph[i]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0, [0])
        return res