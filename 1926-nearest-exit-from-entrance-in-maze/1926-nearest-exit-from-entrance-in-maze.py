class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        # bfs find shortest distance
        # collect exits except for entrance
        # start from entrance, if r, c == exit: return distance
        # 04: 00
        ROWS, COLS = len(maze), len(maze[0])
        q = deque([entrance])
        visited = set([tuple(entrance)])
        distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        exits = set() # TODO
        for c in range(COLS):
            if maze[0][c] == ".":
                exits.add((0, c))
            if maze[ROWS - 1][c] == ".":
                exits.add((ROWS - 1, c))
        for r in range(ROWS):
            if maze[r][0] == ".":
                exits.add((r, 0))
            if maze[r][COLS - 1] == ".":
                exits.add((r, COLS - 1))
        if tuple(entrance) in exits: exits.remove(tuple(entrance))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in exits: return distance 
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        (nr, nc) in visited or maze[nr][nc] == "+"): continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
            distance += 1
        return -1