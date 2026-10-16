class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        colors = [0] * (n + 1)
        adj = defaultdict(list)
        for start, end in dislikes:
            adj[start].append(end)
            adj[end].append(start)

        def bfs(i):
            colors[i] = 1
            q = deque([i])
            while q:
                elem = q.popleft()
                for nei in adj[elem]:
                    if colors[nei] == 0: 
                        colors[nei] = -colors[elem]
                        q.append(nei)
                    elif colors[nei] == colors[elem]:
                        return False
            return True
                    
        for i in range(1, n + 1):
            if colors[i] == 0:
                if not bfs(i): return False
        return True