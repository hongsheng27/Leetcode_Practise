class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        minHeap = [] # (end, passengers)
        cur = 0
        for passengers, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                e, p = heapq.heappop(minHeap)
                cur -= p
            heapq.heappush(minHeap, (end, passengers))
            cur += passengers
            if cur > capacity: return False
        return True

