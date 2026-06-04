class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        l = 0
        minRange = (0, float('inf')) # l, r
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        have = 0
        for r in range(len(s)):
            if s[r] in count: 
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    have += 1
            while have == len(count):
                if r - l < minRange[1] - minRange[0]:
                    minRange = (l, r)
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        have -= 1
                l += 1
        if minRange[1] == float('inf'): return "" 
        return s[minRange[0]: minRange[1] + 1]



        