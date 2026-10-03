class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # using fixwindow which length == needle, to find string in haystack
        # if space not enough, return -1
        n = len(needle)
        for l in range(len(haystack) - n + 1):
            r = l + n
            if haystack[l: r] == needle:
                return l
        return -1
            