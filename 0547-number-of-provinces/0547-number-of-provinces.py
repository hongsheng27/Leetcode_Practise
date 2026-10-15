class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        n = COLS
        par, rank = {}, {}
        for i in range(n):
            par[i] = i
            rank[i] = 0

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return 1
        
        for r in range(ROWS):
            for c in range(r, COLS):
                if isConnected[r][c] == 1:
                    n -= union(r, c)
        return n
