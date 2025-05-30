class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [[] for _ in range(len(s) + 1)]
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)
        for value, cnt in count.items():
            freq[cnt].append(value)
        res = ""
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res += (j * i)
        return res

