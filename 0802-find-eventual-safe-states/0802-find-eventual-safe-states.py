class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        # dfs + visited to find safe node, try to use memo if find a safe node in the middle
        # need some try
        # 08: 10
        n = len(graph)
        state = [0] * n # 0 unsure, 1 progressing, 2 safe, 3 unafe
        def dfs(node):
            if state[node] == 2: return  True
            if state[node] == 1 or state[node] == 3: return False
            if graph[node] == []: 
                state[node] = 2
                return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    state[node] = 3
            if state[node] != 3: state[node] = 2
            return state[node] == 2

        for i, s in enumerate(state):
            if s == 0:
                dfs(i)
        print(state)
        res = []
        for i, s in enumerate(state):
            if s == 2:
                res.append(i)
        return res
        