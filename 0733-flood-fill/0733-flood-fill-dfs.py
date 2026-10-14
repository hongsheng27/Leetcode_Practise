class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # dfs / bfs(sr, sc)
        # if over range or != start color => continue
        ROWS, COLS = len(image), len(image[0])
        startColor = image[sr][sc]
        if startColor == color: return image
        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != startColor: return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image