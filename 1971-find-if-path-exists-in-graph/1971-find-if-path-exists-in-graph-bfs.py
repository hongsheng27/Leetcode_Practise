class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set([source])
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination: return True
            for nei in adj[node]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)
        return False
