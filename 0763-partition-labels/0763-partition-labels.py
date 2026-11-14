class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        start = end = 0
        res = []
        for r in range(len(s)):
            end = max(end, lastIndex[s[r]])

            if r == end:
                res.append(end - start + 1)
                start = end + 1
        return res
                

