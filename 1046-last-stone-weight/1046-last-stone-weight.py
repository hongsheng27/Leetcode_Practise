class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            largestStone = -heapq.heappop(maxHeap)
            secondLargestStone = -heapq.heappop(maxHeap)
            remaining = largestStone - secondLargestStone
            if remaining:
                heapq.heappush(maxHeap, -remaining)
        return -maxHeap[0] if maxHeap else 0
        