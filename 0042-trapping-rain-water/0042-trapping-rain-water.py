class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        pref = [0] * len(height)
        suff = [0] * len(height)

        for i in range(1, n):
            pref[i] = max(pref[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i + 1])
        for i in range(1, n - 1):
            water = max(0, min(pref[i], suff[i]) - height[i])
            res += water
        return res

