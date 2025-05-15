# Brute Force
class Solution(object):
    def trap(self, height):
        res = 0
        for i, bar in enumerate(height):
            left_heightest = max(height[:i]) if height[:i] else 0
            right_heightest = max(height[i+1:]) if height[i +1:] else 0
            bar_volumn = max(0, min(left_heightest, right_heightest) - bar)
            res += bar_volumn
        return res
