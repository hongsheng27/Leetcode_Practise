class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counter = Counter(s)
        start = 0
        seen = set([s[start]])
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
            counter[c] -= 1
            print('@', c, counter[c])
            if c in seen and counter[c] == 0:
                seen.remove(c)

            print(counter, seen)
            if len(seen) == 0: 
                res.append(i - start + 1)
                start = i + 1
                if start < len(s):
                    seen.add(s[start])
        return res

