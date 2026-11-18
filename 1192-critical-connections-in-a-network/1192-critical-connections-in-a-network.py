class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        disc = [-1] * n
        low = [-1 ]* n

        adj = defaultdict(list)
        for first, second in connections:
            adj[first].append(second)
            adj[second].append(first)

        time = 0
        res = []
        def dfs(i, parent):
            nonlocal time
            if disc[i] != -1: return
            disc[i] = time
            low[i] = time
            time += 1
            for nei in adj[i]:
                if nei == parent: continue
                dfs(nei, i)
                low[i] = min(low[nei], low[i])
                if low[nei] > disc[i]:
                    res.append([nei, i])

        dfs(0, None)
        print(low)
        return res