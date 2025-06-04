class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        max_len = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_len = max(max_len, len(charSet))
        return max_len
        