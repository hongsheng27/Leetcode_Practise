class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # heap => sort first
        # put leave time to minHeap, if new start time have overlap with earily leave, add it to capacity,
        # otherwise, heappop()
        # if over capacity, than return False
        # clean period end earily
        trips.sort(key = lambda x: x[1])
        minHeap = []
        people = 0
        for amount, start, end in trips:
            while minHeap and start >= minHeap[0][0]:
                e, a = heapq.heappop(minHeap)
                people -= a

            heapq.heappush(minHeap, (end, amount))
            people += amount

            if people > capacity: return False
        return True



         