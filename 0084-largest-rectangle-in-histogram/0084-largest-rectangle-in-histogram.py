class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prefix = [-1] * n
        suffix = [n] * n 

        stack = []
        # suffix
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                suffix[index] = i
            stack.append(i)
        # prefix
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                prefix[index] = i
            stack.append(i)

        maxArea = 0
        # calculation
        for i in range(n):
            width = suffix[i] - prefix[i] - 1
            height = heights[i]
            area = width * height
            maxArea = max(maxArea, area)
        return maxArea

