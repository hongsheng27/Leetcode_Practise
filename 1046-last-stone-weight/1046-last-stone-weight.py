class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            firstLarge = heapq.heappop(maxHeap)
            secondLarge = heapq.heappop(maxHeap)
            remaining = -firstLarge - (-secondLarge)
            if remaining:
                heapq.heappush(maxHeap, -remaining)
        return -maxHeap[0] if maxHeap else 0