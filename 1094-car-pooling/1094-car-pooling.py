class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # put trip in minHeap # end, amount
        # if overlap, check if over capacity, return False
        # otherwise popleft()
        ppl = 0
        minHeap = []
        trips.sort(key=lambda x: x[1])
        for passengers, start, end in trips:
            while minHeap and start >= minHeap[0][0]:
                e, p = heapq.heappop(minHeap)
                ppl -= p

            heapq.heappush(minHeap, (end, passengers))
            ppl += passengers
 
            if ppl > capacity: return False
        return True
           