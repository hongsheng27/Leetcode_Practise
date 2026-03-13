# Brute force solution
# Time complexity: O(n^3)
# Space complexity: O(1)
# Can't pass the Leetcode since the time limit

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_area = 0
        for i in range(len(heights) + 1):
            for j in range(i+1, len(heights) + 1):
                area = (j - i) *  min(heights[i:j])
                if area > biggest_area:
                    biggest_area = area
        return biggest_area
