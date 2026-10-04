class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # build lps
        lps = [0] * len(needle)
        length = 0
        i = 1
        while i < len(needle):
            if needle[length] == needle[i]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        # KMP search
        i = 0 # haystack pointer
        j = 0 # needle pointer
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
        return -1
        