class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        top = 0
        bottom = len(grid) - 1
        left = 0
        right = len(grid[0]) - 1
        while left < right and top < bottom:
            q = deque()
            for col in range(left, right):
                q.append(grid[top][col])
            for row in range(top, bottom):
                q.append(grid[row][right])
            for col in range(right, left, -1):
                q.append(grid[bottom][col])
            for row in range(bottom, top, -1):
                q.append(grid[row][left])
            k2 = k % len(q)
            for i in range(k2):
                q.append(q.popleft())
            index = 0
            for col in range(left, right + 1):
                grid[top][col] = q.popleft()
            top += 1
            for row in range(top, bottom + 1):
                grid[row][right] = q.popleft()
            right -= 1
            for col in range(right, left - 1, -1):
                grid[bottom][col] = q.popleft()
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                grid[row][left] = q.popleft()
            left += 1
        return grid

        
        
            