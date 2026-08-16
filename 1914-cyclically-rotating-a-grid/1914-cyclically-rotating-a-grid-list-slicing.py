class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        top = 0
        bottom = len(grid) - 1
        left = 0
        right = len(grid[0]) - 1
        while left < right and top < bottom:
            lst = []
            for col in range(left, right):
                lst.append(grid[top][col])
            for row in range(top, bottom):
                lst.append(grid[row][right])
            for col in range(right, left, -1):
                lst.append(grid[bottom][col])
            for row in range(bottom, top, -1):
                lst.append(grid[row][left])
            k2 = k % len(lst)
            print(lst)
            lst = lst[k2:] + lst[:k2]
            print(lst)
            index = 0
            for col in range(left, right + 1):
                grid[top][col] = lst[index]
                index += 1
            top += 1
            for row in range(top, bottom + 1):
                grid[row][right] = lst[index]
                index += 1
            right -= 1
            for col in range(right, left - 1, -1):
                grid[bottom][col] = lst[index]
                index += 1
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                grid[row][left] = lst[index]
                index += 1
            left += 1
        return grid

        
        
            