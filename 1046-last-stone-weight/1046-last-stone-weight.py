class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            maxWeight, secMaxWeight = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            newWeight = maxWeight - secMaxWeight 
            heapq.heappush(maxHeap, -newWeight)
        return -maxHeap[0]


        