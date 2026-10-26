class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window: move right to become legal, move left until illgal, record ans(l, r) when legal
        # while becomes illgal, start expending right, repeat 1 step
        # maintain map like {'A': 2, 'B': 1}, and have == 2 to save number of elem,  every time meet target, minus 1, if it beomces zero, have -= 1
        if len(t) > len(s): return ""
        count = defaultdict(int)
        for c in t:
            count[c] += 1
        have = l = 0
        res = (0, float('inf'))

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0: have += 1
            
            while have == len(count):
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1: have -= 1
                if r - l < res[1] - res[0]:
                    res = (l, r)
                l += 1 
        return "" if res[1] == float('inf') else s[res[0]: res[1] + 1]


