class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        pref, suff = [0] * len(height), [0] * len(height)
        for i in range(1, len(height)):
            pref[i] = max(pref[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i + 1])
        for i in range(1, len(height) - 1):
            h = min(pref[i], suff[i])
            res += max(0, h - height[i])
        return res