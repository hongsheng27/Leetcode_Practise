class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # dfs + visited to find safe node, try to use memo if find a safe node in the middle
        n = len(graph)
        # 0: Unknown
        # 2: Safe
        # 3: Unsafe
        state = [0] * n 
        def dfs(node):
            if state[node] == 2: return  True
            if state[node] == 3: return False
            state[node] = 3
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        for i, s in enumerate(state):
            if s == 0:
                dfs(i)
        res = []
        for i, s in enumerate(state):
            if s == 2:
                res.append(i)
        return res
        