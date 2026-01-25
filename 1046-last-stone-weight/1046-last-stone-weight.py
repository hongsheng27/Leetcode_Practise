class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            remaining = (-first) - (-second)
            heapq.heappush(maxHeap, -remaining)
        return -maxHeap[0]