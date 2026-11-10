class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort() # pointer i
        s.sort() # pointer j
        i = j = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                j += 1
                i += 1
            else:
                j += 1
        return i
