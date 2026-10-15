class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # edges => adjsant list
        # start from source, if node == destination: return True
        # or return False
        # 5:00
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set([source])
        def dfs(elem):
            if elem == destination: return True
            res = False
            for nei in adj[elem]:
                if nei in visited: continue
                visited.add(nei)
                if dfs(nei): res = True
            return res
        return dfs(source)
        # 10: 00 debug
        # dfs(elme) wrong => dfs(nei)
        # 20:00 ai debug => add bi-directional graph
