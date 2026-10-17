class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # directed graph, start from 0
        # len of visited == rooms, return True
        # bfs / dfs
        visited = set()
        def dfs(i):
            visited.add(i)
            for nei in rooms[i]:
                if nei not in visited:
                    dfs(nei)
        dfs(0) 
        return len(visited) == len(rooms)