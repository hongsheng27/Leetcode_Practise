class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # maintain colors to split
        # traverse  n people
        # if n has not group => 1. traverse nei, make it group be -group, dfs keep going
        # 2. nei has group => return False if n group == nei group
        # 10: 00
        # solution2: maybe not dfs/bfs
        # travese dislikes, and fill colors
        # if start has no color, fill 1, end become -color
        # if start has color, end become -color
        # if end colors == start colors: return False
        # 16:00
        # colors = [0] * (n + 1)
        # for start, end in dislikes:
        #     if colors[start] == 0:
        #         colors[start] = 1
        #         colors[end] = -colors[start]
        #     else:
        #         if colors[end] == 0:
        #             colors[end] = -colors[start]
        #         elif colors[end] == colors[start]:
        #             return False
        # return True
        # 20:00 debug
        # solution3: I still need dfs/bfs, graph route exist in dislike
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
        # 38:00 done
        # 39 ai debug  1. colors[i] == 1 2.if bfs(i): return False
