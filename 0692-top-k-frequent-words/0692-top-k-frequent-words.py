class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        maxHeap = []

        for word, time in list(count.items()):
            heapq.heappush(maxHeap, (-time, word))
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res



        