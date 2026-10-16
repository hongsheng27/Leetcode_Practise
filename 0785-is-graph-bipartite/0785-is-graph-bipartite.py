class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        # solution1: adj node should be different group
        # traverse every node to check if unconnected node
        # if no group => group 1, nei becomes opposite until basecase
        # if it have group => 1. see if nei group equal itself, if so, return False
        # 2. if nei has not group, it becomes opposite of group
        # visited to make sure go back itself, but need to see visited node
        n = len(graph)
        colors = [0] *  n

        def bfs(i):
            colors[i] = 1
            q = deque([i])
            while q:
                elem = q.popleft()
                for nei in graph[elem]: 
                    if colors[nei] == 0:
                        q.append(nei)
                        colors[nei] = -colors[elem]
                    elif colors[elem] == colors[nei]: 
                        return False
            return True

        for i in range(n):
            if colors[i] == 0:
                if not bfs(i):
                    return False
        return True