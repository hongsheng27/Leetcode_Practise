class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # from source to destination, the tuition way is dfs, I forget the compecity
        # second solution will be bfs
        # 7 : 24
        # 20: 47 realize it is non-directed graph
        # add visited and adj[end].append(start)
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()
        def dfs(n):
            if n in visited: return False
            if n == destination: return True

            visited.add(n)
            for nei in adj[n]:
                if dfs(nei):
                    return True
            return False
        return dfs(source)
        # 23:36 done