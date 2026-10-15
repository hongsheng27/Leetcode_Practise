class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(city):
            visited.add(city)
            for nei in range(n):
                if nei not in visited and isConnected[city][nei] == 1:
                    dfs(nei)

        res = 0
        for city in range(n):
            if city not in visited:
                res += 1
                dfs(city)
        return res