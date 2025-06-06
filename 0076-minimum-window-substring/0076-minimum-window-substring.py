class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tCounter = Counter(t)
        windowCounter = defaultdict(int)
        formed = 0
        l = 0 
        res = (0, float(inf))
        for r in range(len(s)):
            windowCounter[s[r]] += 1
           
            if s[r] in tCounter and windowCounter[s[r]] <= tCounter[s[r]]:
                formed += 1
            while formed == len(t):
                if r - l < res[1] - res[0]:
                    res = (l, r)
                    print(res)
                windowCounter[s[l]] -= 1
                if s[l] in tCounter and windowCounter[s[l]] < tCounter[s[l]]:
                    formed -= 1
                l += 1
        return "" if res[1] == float("inf") else s[res[0]: res[1] + 1]
                
               
            
            
                



                
