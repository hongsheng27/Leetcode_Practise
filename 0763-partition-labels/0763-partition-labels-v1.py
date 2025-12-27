class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndexCount = {}
        end = size = 0
        for i, c in enumerate(s):
            lastIndexCount[c] = i
        for i, c in enumerate(s):
            end = max(end, lastIndexCount[c])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res


