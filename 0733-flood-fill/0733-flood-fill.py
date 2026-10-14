class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # bfs(sr, sc), since want all connected color, dfs might not be good choice
        # if over range or != start color => continue
        ROWS, COLS = len(image), len(image[0])
        q = deque([(sr, sc)])
        startColor = image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr == ROWS or nc < 0 or
                    nc == COLS or image[nr][nc] != startColor or (nr, nc) in visited): continue
                q.append((nr, nc))
                visited.add((nr, nc))
        return image

        