class Word:
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.name > other.name
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        minHeap = []
        count = Counter(words)
        for word, freq in count.items():
            heapq.heappush(minHeap, Word(word, freq))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap).name)
        return res[::-1]
