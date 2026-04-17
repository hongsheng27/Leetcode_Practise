class Solution:
    def trap(self, height: List[int]) -> int:
        l = leftMax = rightMax = 0
        r = len(height) - 1
        total = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                l += 1
                total += max(0, leftMax - height[l])
            else:   
                r-= 1
                total += max(0, rightMax - height[r])
        return total