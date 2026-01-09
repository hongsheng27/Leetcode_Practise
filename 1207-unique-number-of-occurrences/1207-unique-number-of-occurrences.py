class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = 1 + count.get(i, 0)
        freq = count.values()
        return len(freq) == len(set(freq))