class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(i):
            if i == n or i in visited: return

            visited.add(i)
            for nei in rooms[i]:
                dfs(nei)
        dfs(0)
        return len(visited) == n