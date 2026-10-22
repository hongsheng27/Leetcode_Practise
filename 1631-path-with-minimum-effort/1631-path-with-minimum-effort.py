class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # dijkstra 
        # minHeap to pop smaller difference, push nei with max difference
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)] # difference, r, c
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        while minHeap:
            difference, r, c = heapq.heappop(minHeap)
            if (r, c) in visited: continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1: return difference
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS: continue
            
                maxDiff = max(abs(heights[nr][nc] - heights[r][c]), difference)
                heapq.heappush(minHeap, (maxDiff, nr, nc))



