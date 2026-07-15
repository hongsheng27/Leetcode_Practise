class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) >= 2:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            remaining = -first - (-second)
            if remaining:
                heapq.heappush(maxHeap, -remaining)
        return -maxHeap[0] if maxHeap else 0
            