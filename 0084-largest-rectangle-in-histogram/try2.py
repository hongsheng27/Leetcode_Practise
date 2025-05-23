# Brute force solution2 
# Time complexity: O(n^2)
# Space complexity: O(n^2)
# # Can't pass the Leetcode since the time limit
# build a 2D min_table to store the minimum value in the range [i, j]
# i.g. min_table = [[0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0],
#              [0, 0, 0, 0, 0]]
# min_table[i][j] = min(heights[i:j])

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_area = 0
        n = len(heights)
        min_table = [[-1] * n for _ in range(n)] 

        for i in range(n):
            min_val = heights[i]
            for j in range(i, n):
                min_val = min(min_val, heights[j])
                min_table[i][j] = min_val
    
        for i in range(n):
            for j in range(i, n):
                width = j - i + 1
                height = min_table[i][j]
                area = width * height
                if area > biggest_area:
                    biggest_area = area
        return biggest_area