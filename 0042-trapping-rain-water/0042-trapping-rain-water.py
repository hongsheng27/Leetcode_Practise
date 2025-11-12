class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] <= h:
                mid = stack.pop()[1]
                if stack:
                    left = stack[-1][1]
                    right = h
                    _h = min(left, right) - mid
                    w = i - stack[-1][0] - 1
                    res += _h * w 
            stack.append((i, h))
        return res
        