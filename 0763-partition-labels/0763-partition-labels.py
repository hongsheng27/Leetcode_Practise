class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndexMap = {}
        for i, c in enumerate(s):
            lastIndexMap[c] = i
        l = r = 0
        res = []
        goal = lastIndexMap[s[0]]
        while r < len(s):
            goal = max(goal, lastIndexMap[s[r]])
            if r == goal:
                res.append(r - l + 1)
                l = r + 1
            r += 1
        return res