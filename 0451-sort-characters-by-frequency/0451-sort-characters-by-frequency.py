class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(list)
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)
        for value, cnt in count.items():
            freq[cnt].append(value)
        res = []
        print(freq)
        for i in range(len(s), 0, -1):
            for j in freq[i]:
                res.append(j * i)
        return "".join(res)

