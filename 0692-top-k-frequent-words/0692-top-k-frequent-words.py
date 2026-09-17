class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        minHeap = []

        for word, time in list(count.items()):
            heapq.heappush(minHeap, Word(word, time))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap).word)
       
        return res[::-1]



        