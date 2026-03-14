class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rightmost = [n] * n
        leftmost = [-1] * n
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rightmost[index] = i
            stack.append((i, h))
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                leftmost[index] = i
            stack.append((i, heights[i]))
        maxArea = 0
        for i in range(n):
            width = rightmost[i] - leftmost[i] - 1
            area = width * heights[i]
            maxArea = max(maxArea, area)
        return maxArea
            

