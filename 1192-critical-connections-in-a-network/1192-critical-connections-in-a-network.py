class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        disc = [-1] * n
        low = [0] * n
        time = 0
        res = []
        adj = defaultdict(list)
        for first, second in connections:
            adj[first].append(second)
            adj[second].append(first)

        def dfs(node, parent):
            nonlocal time
            disc[node] = low[node] = time
            time += 1
            for nei in adj[node]:
                if nei == parent: continue
                if disc[nei] == -1:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > disc[node]:
                        res.append([node, nei])
                else:
                    low[node] = min(low[node], disc[nei])

            
        dfs(0, None)
        return res

        