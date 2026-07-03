class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        res = []
        r = time = farthest = 0
        while r < len(s):
            time += 1
            farthest = max(farthest, lastIndex[s[r]])
            if r == farthest:
                res.append(time)
                time = 0
            r += 1
        return res
             