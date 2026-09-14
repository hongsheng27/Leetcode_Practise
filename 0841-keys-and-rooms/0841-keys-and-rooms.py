class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = available = len(rooms)
        visited = set()
        def dfs(i):
            nonlocal available
            if i == n or i in visited: return
            available -= 1
            visited.add(i)
            for nei in rooms[i]:
                dfs(nei)
        dfs(0)
        return available == 0