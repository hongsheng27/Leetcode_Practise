class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        l = have = 0
        ans = ""
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    have += 1
            while have == len(count):
                if not ans or r - l + 1 < len(ans):
                    ans = s[l: r + 1]
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        have -= 1
                l += 1
        return ans
            
                


        