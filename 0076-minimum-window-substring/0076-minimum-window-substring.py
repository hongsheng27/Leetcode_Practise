class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        count = {}
        for i in t:
            if i not in count:
                count[i] = 0
            count[i] += 1
        having = len(count)
    
        r = l = 0
        minRange = (0, float('inf'))
        while r < len(s):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0: having -= 1
            while not having:
                if r - l < minRange[1] - minRange[0]:
                    minRange = (l, r)
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1: having += 1
                l += 1
            r += 1
        
        return s[minRange[0]: minRange[1] + 1] if minRange[1] != float('inf') else ""
            
            
        