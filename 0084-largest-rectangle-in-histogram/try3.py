# Brute force solution3
# Time complexity: O(n^2)
# Space complexity: O(1)
# # Can't pass the Leetcode since the time limit
# not saving 2D min_table to achieve O(1) space complexity

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_area = 0
        n = len(heights)
 
        for i in range(n):
            min_val = heights[i]
            for j in range(i, n):
                min_val = min(min_val, heights[j])
                width = j - i + 1
                height = min_val
                area = width * height
                biggest_area = max(biggest_area, area)
    
        return biggest_area
        
