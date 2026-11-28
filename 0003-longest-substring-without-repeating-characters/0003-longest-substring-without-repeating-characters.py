class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            while c in count:
                count[s[l]] -= 1
                if count[s[l]] == 0: del count[s[l]]
                l += 1
            count[c] = count.get(c, 0) + 1
            res = max(res, r - l + 1)
        return res
        