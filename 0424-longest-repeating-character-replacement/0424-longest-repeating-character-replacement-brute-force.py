class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        length = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                count[s[r]] = count.get(s[r], 0) + 1
                if (r - l + 1) - max(count.values()) <= k:
                    length = max(length, r - l + 1)
            count = {}
        return length