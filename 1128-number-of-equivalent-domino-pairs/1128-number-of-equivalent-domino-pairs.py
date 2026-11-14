class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        freq = defaultdict(int)
        for first, second in dominoes:
            key = (min(first, second), max(first, second))
            freq[key] += 1
        res = 0
        for i in freq.values():
            if i > 1:
                res += (i * (i - 1) // 2)
        return res