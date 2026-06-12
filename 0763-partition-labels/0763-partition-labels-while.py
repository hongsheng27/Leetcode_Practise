class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        l = r = 0
        while r < len(s):
            end = lastIndex[s[l]]
            while r <= end:
                end = max(end, lastIndex[s[r]])
                if r == end:
                    res.append(r - l + 1)
                    l = r + 1
                r += 1
        return res
