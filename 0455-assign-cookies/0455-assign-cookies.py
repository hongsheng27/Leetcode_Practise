class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        for i in range(len(s)):
            if j < len(g) and s[i] >= g[j]:
                j += 1
        return j


            