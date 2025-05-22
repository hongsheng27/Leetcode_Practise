class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggnest_area = 0
        n = len(heights)
        rightmost_lst = [n - 1] * n 
        leftmost_lst = [0] * n 
        stack = []
        stack2 = []
        for i in range(n):
            while stack and heights[i] < stack[-1][1]:
                [index, height] = stack.pop()
                rightmost_lst[index] = i - 1
            stack.append([i, heights[i]])
        for i in range(n - 1, -1, -1):
            while stack2 and heights[i] < stack2[-1][1]:
                [index, height] = stack2.pop()
                leftmost_lst[index] = i + 1
            stack2.append([i, heights[i]])
        print(leftmost_lst, rightmost_lst)
        for i in range(n):
            height = heights[i]
            width = rightmost_lst[i] - leftmost_lst[i] + 1
            area = height * width
            biggnest_area = max(area, biggnest_area)
    
        return biggnest_area
        