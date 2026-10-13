class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0] * n # 0 no group, 1 first group, 2 second group
        for i in range(n):
            if color[i] != 0: continue

            q = deque([i])
            color[i] = 1
            
            while q:
                elem = q.popleft()
                for nei in graph[elem]:
                    if color[nei] == 0:
                        color[nei] = -color[elem]
                        q.append(nei)
                    elif color[nei] == color[elem]:
                        return False
        return True
                        



                        