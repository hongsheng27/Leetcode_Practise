class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lenH = len(heights)
        leftMost, rightMost = [-1] * lenH, [lenH] * lenH
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rightMost[index] = i
            stack.append((i, h))
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while stack and stack[-1][1] > h:
                index, heihgt = stack.pop()
                leftMost[index] = i
            stack.append((i, heights[i]))
        maxArea = 0
        for i in range(lenH):
            width = rightMost[i] - leftMost[i] - 1
            maxArea = max(maxArea, width * heights[i])
        return maxArea


        