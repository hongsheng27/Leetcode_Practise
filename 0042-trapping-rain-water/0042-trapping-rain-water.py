class Solution(object):
    def trap(self, height):
        if not height: return 0
        res = 0
        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        
        while l < r:
            if height[l] <= height[r]:
                l += 1
                water = max(0, left_max - height[l])
                res += water
                left_max = max(left_max, height[l])
            elif height[l] > height[r]:
                r -= 1
                water = max(0, right_max - height[r])
                res += water
                right_max = max(right_max, height[r]) 
        
        return res
