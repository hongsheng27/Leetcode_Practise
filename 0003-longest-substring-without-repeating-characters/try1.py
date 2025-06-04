class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = {}
        length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in count:
                del count[s[l]]
                l += 1
            count[s[r]] = r
            length = max(length, len(count))
        length = max(length, len(count))
        return length
        