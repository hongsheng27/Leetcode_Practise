class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n = len(isConnected)
        # only need to see hald
        # except diagonal line, one 1 mean n - 1
        # 08: 00
        ROWS, COLS = len(isConnected), len(isConnected[0])
        n = len(isConnected)
        adj = defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1:
                    adj[r].append(c)
                    adj[c].append(r)
        visited = set()
        res = 0
        def dfs(ith):
            for nei in adj[ith]:
                if nei in visited: continue
                visited.add(nei)
                dfs(nei)
        for i in range(n):
            if i not in visited: 
                visited.add(i)
                dfs(i)
                res += 1
        return res
        # 14: 18 done debug
        # 37 ai-help: 
        # 1. forget add  if isConnected[r][c] == 1: