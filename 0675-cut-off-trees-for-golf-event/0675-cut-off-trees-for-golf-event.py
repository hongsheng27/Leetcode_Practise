class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        ROWS, COLS = len(forest), len(forest[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        trees = [] # height, r, c
        for r in range(ROWS):
            for c in range(COLS):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()

        def bfs(start, target):
            q = deque([start])
            visited = set([start])
            steps = 0
            
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if (r, c) == target: 
                        return steps
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or 
                            (nr, nc) in visited or forest[nr][nc] == 0):
                            continue
                        q.append((nr, nc))
                        visited.add((nr, nc))
                steps += 1
            return -1

        start = (0, 0)
        res = 0
        for height, r, c in trees:
            steps = bfs(start, (r, c))
            if steps == -1:
                return -1
            res += steps
            start = (r, c)
        return res