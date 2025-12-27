class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counter = Counter(s)
        start = 0
        seen = set()
        for i, c in enumerate(s):
            seen.add(c)
            counter[c] -= 1
            if counter[c] == 0:
                seen.remove(c)

            if not seen: 
                res.append(i - start + 1)
                start = i + 1
        return res

