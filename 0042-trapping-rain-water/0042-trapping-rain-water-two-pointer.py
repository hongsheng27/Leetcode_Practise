class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if height[l] <= height[r]:
                leftMax = max(leftMax, height[l])
                l += 1
                water = max(0, leftMax - height[l])
            else:
                rightMax = max(rightMax, height[r])
                r -= 1
                water = max(0, rightMax - height[r])
            res += water
        return res