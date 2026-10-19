class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # dfs + visited to find safe node, try to use memo if find a safe node in the middle
        n = len(graph)
        safe = {}
        def dfs(node):
            if node in safe: return safe[node]
            safe[node] = False
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node] = True
            return safe[node]
        res = []
        for i in range(n):
            if dfs(i): res.append(i)
        return res
        