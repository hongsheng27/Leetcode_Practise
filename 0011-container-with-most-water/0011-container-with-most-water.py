class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_area = max(max_area, w * h)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        