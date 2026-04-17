class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0 
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                ground = height[stack.pop()]
                if stack:
                    l = height[stack[-1]]
                    r = height[i]
                    h = max(0, min(l, r) - ground)
                    w = i - stack[-1] - 1
                    res += w * h
            stack.append(i)
        return res