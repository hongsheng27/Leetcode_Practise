class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rightmost = [n] * n 
        leftmost = [-1] * n 
        stack = []

        for i in range(n):
            while stack and heights[i] < stack[-1][1]:
                [index, height] = stack.pop()
                rightmost[index] = i
            stack.append([i, heights[i]])

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[i] < stack[-1][1]:
                [index, height] = stack.pop()
                leftmost[index] = i
            stack.append([i, heights[i]])

        max_area = 0
        for i in range(n):
            width = rightmost[i] - leftmost[i] - 1
            area = heights[i] * width
            max_area = max(area, max_area)
    
        return max_area
        