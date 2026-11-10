class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort() # pointer r
        s.sort() # pointer l
        l = r = 0
        while l < len(s) and r < len(g):
            while l < len(s) and s[l] < g[r]:
                l += 1
            if l >= len(s): return r
            l += 1
            r += 1
        return r
