class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # solution 1: heap, save (count, number) tc n log k
        # solution 2: bucket list: 1 - len(n) bucket,o(n)
        minHeap = []
        for number, cnt in Counter(nums).items():
            heapq.heappush(minHeap, (cnt, number))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res
