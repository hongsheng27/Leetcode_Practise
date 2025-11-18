class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        window = set()
        l = 0

        for c in s:
            while c in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            length = max(length, len(window))
        return length
        