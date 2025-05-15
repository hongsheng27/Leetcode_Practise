class Solution(object):
    def trap(self, height):
        if not height: return 0
        res = 0
        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        
        while l < r:
            if left_max <= right_max:
                l += 1
                water = max(0, left_max - height[l])
                res += water
                left_max = max(left_max, height[l])
            elif left_max > right_max:
                r -= 1
                water = max(0, right_max - height[r])
                res += water
                right_max = max(right_max, height[r]) 
        
        return res
