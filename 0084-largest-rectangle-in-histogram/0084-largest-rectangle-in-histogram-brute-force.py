# Brute force solution
# Time complexity: O(n^3)
# Space complexity: O(1)
# Can't pass the Leetcode since the time limit

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            right = i
            while right + 1 < len(heights) and heights[right + 1] >= heights[i]:
                right += 1
            left = i
            while left - 1 >= 0 and heights[left - 1] >= heights[i]:
                left -= 1
            width = right - left + 1
            maxArea = max(maxArea, width * heights[i])
        return maxArea            
