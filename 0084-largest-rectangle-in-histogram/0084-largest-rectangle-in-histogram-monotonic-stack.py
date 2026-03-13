class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, (i - index) * height)
            
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea