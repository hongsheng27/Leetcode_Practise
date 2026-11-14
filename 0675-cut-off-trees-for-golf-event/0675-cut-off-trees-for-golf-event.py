class Solution:
    def cutOffTree(self, forest: list[list[int]]) -> int:
        # collects the tree order list O(M * N)
        # sort trees O(K log K), k means k trees
        # implement K time bfs O(K * (M * N))
        # each bfs: return steps, if can not reach, return -1
        # tc: k * M * N + K log K
        # sc: M * N
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
                            (nr, nc) in visited or forest[nr][nc] == 0): continue
                        visited.add((nr,nc))
                        q.append((nr, nc))
                steps += 1
            return -1

        res = 0
        start = (0, 0)
        for height, r, c in trees:
            steps = bfs(start, (r, c))
            if steps == -1:
                return -1
            res += steps
            start = (r, c)
        return res