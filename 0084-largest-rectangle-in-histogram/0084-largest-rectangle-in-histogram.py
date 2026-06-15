class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftMost = [-1] * n
        rightMost = [n] * n 

        # rightMost
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                rightMost[index] = i
            stack.append(i)
        # leftMost
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                leftMost[index] = i
            stack.append(i)

        maxArea = 0
        # calculation
        for i in range(n):
            width = rightMost[i] - leftMost[i] - 1
            height = heights[i]
            area = width * height
            maxArea = max(maxArea, area)
        return maxArea

